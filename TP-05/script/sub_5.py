from pub import Subcriptor
from pub import Publicador
from datetime import datetime
from pathlib import Path
import sqlite3
import paho.mqtt.client as mqtt
import time
import config as con
import csv

def parceo_string(topic:str,texto:str):
    sala = ""
    sensor = ""
    valor = 0
    lista_topic = topic.split('/') # Genero una lista de los string separados por /
    lista_valor = texto.split(' ') #10.5 °C
    valor = float(lista_valor[0])
    sala = lista_topic[1] # salaX
    sensor = lista_topic[3] #hum - temp
    return sala,sensor,valor

def on_connect(client, userdata, flag, rc):
    print("Conectado al broker mqtt desde mosquitto ")
    print(f"Intentando conectarse al topico...")
    client.subscribe(con.TOPIC_ALL)
    print(f"Suscrito a {con.TOPIC_ALL}")
    print("Creando base de datos")
    conexion = sqlite3.connect(con.DB)
    try:
        conexion.execute("""
            create table datos (
                         sala text,
                         sensor text,
                         valor integer
                         )
        """)
        print("Se creo la tabla de datos")
    except sqlite3.OperationalError:
        print("La tabla de datos ya existe")
        conexion.close()

# Funcion para crear el csv
def on_message(client, userdata, msg):
    texto = msg.payload.decode() # Valor tomado
    
    # Ignorar los comandos
    if texto not in con.LISTA_COMANDOS:
        sala,sensor,valor = parceo_string(msg.topic,texto)
        timestamp = datetime.now().strftime('%H:%M:%S') # Timestamp
        archivo = Path(con.ARCHIVO)
        escribir_header = not archivo.exists() or archivo.stat().st_size == 0 # Escribir encabezado del CSV

        with open(con.ARCHIVO,con.MODO, newline='') as file:
            escritor = csv.writer(file)
            if escribir_header:
                escritor.writerow(["timestamp","topic", "dato"])
            escritor.writerow([timestamp,msg.topic, texto])

# Creacion del gateway
gateway = Subcriptor(con.TOPIC_ALL,nombre="Gateway General")
gateway.conectar(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
gateway.cliente.on_connect = on_connect
gateway.cliente.on_message = on_message
gateway.cliente.loop_start()

# Creacion del publicador de comandos
pub_comandos = Publicador(con.TOPIC_COMANDOS,"Pub_Comandos")
pub_comandos.connect(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
pub_comandos.cliente.loop_start()

try:
    time.sleep(2)
    while True:
        comando = input("Ingrese un comando [START/STOP]: ").strip().upper()
        if comando in ["START","STOP"]:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Timestamp
            print(f"Comando enviado: {comando}", timestamp)
            pub_comandos.publicar(comando)
        else:
            print("Comando no Reconocido")
        time.sleep(0.5)
except KeyboardInterrupt:
    gateway.desconectar()
    pub_comandos.desconectar()
