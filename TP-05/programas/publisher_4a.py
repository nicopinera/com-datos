import paho.mqtt.client as mqtt
import random
import time
import datetime

#Dispositivo A
# Parametros de coneccion
broker = "localhost"
port = 1883
topic = "lan/deviceA/status"
ttc = 60 #segundos
intervalo = 3 #segundos

#Callback   
def on_connect(client, userdata, flag, rc):
    print("Conectado al broker mqtt desde mosquitto ")
    
dispositivoA = mqtt.Client()
dispositivoA.on_connect = on_connect

dispositivoA.connect(broker, port, ttc)

dispositivoA.loop_start()


try:
    temperatura = 9999
    while True:
        if(temperatura == 9999):
            temperatura = random.uniform(-5.00, 90.0) # Obtiene un valor inicial de temperatura
        temperatura += random.normalvariate(0.00, 2.00) # Varia la temperatura
        temperatura = round(temperatura, 2)
        payload = str(temperatura)+" °C"
        dispositivoA.publish(topic, payload)
        time.sleep(10.0)
except KeyboardInterrupt:
    print("Desconectado del broker")
    dispositivoA.loop_stop()
    dispositivoA.disconnect()
    print("Dispositivo desconectado")

