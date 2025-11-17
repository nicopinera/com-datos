import paho.mqtt.client as mqtt
import config as con
import random
import time

#Dispositivo B Suscriptor

#Callback   
def on_connect(client, userdata, flag, rc):
    if rc == 0:
        print("Conectado al broker mqtt desde mosquitto ")
        print(f"Intentando conectarse al topico...")
        client.subscribe(con.TOPIC_DEVA)
        print(f"Suscrito a {con.TOPIC_DEVA}")
    else:
        print("No se ha podido conectar al broker")

#
def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()}")
    

dispositivoA = mqtt.Client()
dispositivoA.on_connect = on_connect
dispositivoA.on_message = on_message

dispositivoA.connect(con.BROKER, con.PORT, con.TIME_TO_CONNECT)

dispositivoA.loop_forever()