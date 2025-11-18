from pub import Publicador
from pub import Subcriptor
from datetime import datetime
import paho.mqtt.client as mqtt
import time
import config as con
import random

# Primer valor para la generacion de valores aleatorios
temp_1 = -1
temp_2 = -1
hum_1 = -1
hum_2 = -1
simulacion_activa = False # para iniciar o no la simulacion de datos

def valor_sensores(topic):
    global temp_1, temp_2, hum_1,hum_2
    carga = ""
    match topic:
        case "lan/sala1/sensor/temp":
            if temp_1 == None:
                temp_1 = random.uniform(-5.00, 90.0)
            temp_1 += random.normalvariate(0.00, 2.00)
            temp_1 = round(temp_1, 2)
            carga = str(temp_1)+" °C"
        case "lan/sala1/sensor/hum":
            if hum_1 == -1:
                hum_1 = random.uniform(0, 100)
            hum_1 += random.normalvariate(0, 2)
            hum_1 = round(hum_1,0)
            carga = str(hum_1)+" %"
        case "lan/sala2/sensor/temp":
            if temp_2 == -1:
                temp_2 = random.uniform(-5.00, 90.0)
            temp_2 += random.normalvariate(0.00, 2.00)
            temp_2 = round(temp_2, 2)
            carga = str(temp_2)+" °C"
        case "lan/sala2/sensor/hum":
            if hum_2 == -1:
                hum_2 = random.uniform(0, 100)
            hum_2 += random.normalvariate(0, 2)
            hum_2 = round(hum_2,0)
            carga = str(hum_2)+" %"
    return carga

def on_message(client,userdata,msg):
    global simulacion_activa
    comando = msg.payload.decode()
    if comando == "START":
        simulacion_activa = True
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Timestamp
        print("Simulacion activada" , timestamp)
    elif comando == "STOP":
        simulacion_activa = False
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Timestamp
        print("Simulacion detenida", timestamp)


lista_pub = []
index = 0
# Generacion de Publicadores
for i in range(4):
    pub = Publicador(con.LISTA_TOPIC_PUB[index],f"Pub{i+1}")
    pub.connect(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
    pub.cliente.loop_start()
    lista_pub.append(pub)
    index +=1

sub_comandos = Subcriptor(con.TOPIC_COMANDOS,"Sub_comandos")
sub_comandos.cliente.on_message = on_message
sub_comandos.conectar(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
sub_comandos.cliente.loop_start()

try:
    while True:
        if simulacion_activa:
            for i in range(len(lista_pub)):
                pub_actual = lista_pub[i]
                carga = valor_sensores(pub_actual.topic)
                pub_actual.publicar(carga)
                time.sleep(0.5)
        time.sleep(0.5)
except KeyboardInterrupt:
    for i in range(len(lista_pub)):
        pub_actual = lista_pub[i]
        print(f"Desconectando: {pub_actual.nombre} - {pub_actual.topic}")
        pub_actual.desconectar()
    sub_comandos.desconectar()