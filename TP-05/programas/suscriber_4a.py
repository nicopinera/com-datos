import paho.mqtt.client as mqtt
import random
import time

#Dispositivo B Suscriptor
# Parametros de coneccion
broker = "localhost"
port = 1883
topic = "lan/deviceA/status"
ttc = 60 #segundos

#Callback   
def on_connect(client, userdata, flag, rc):
    if rc == 0:
        print("Conectado al broker mqtt desde mosquitto ")
        print(f"Intentando conectarse al topico...")
        client.subscribe(topic)
        print(f"Suscrito a {topic}")
    else:
        print("No se ha podido conectar al broker")

#
def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()}")
    

dispositivoA = mqtt.Client()
dispositivoA.on_connect = on_connect
dispositivoA.on_message = on_message

dispositivoA.connect(broker, port, ttc)

dispositivoA.loop_forever()