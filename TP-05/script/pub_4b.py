from pub import Publicador
import paho.mqtt.client as mqtt
import time
import config as con
import random

pub = Publicador(nombre="Pub_Ej_4b")
pub.connect(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
pub.cliente.loop_start()

try:
    temperatura = -1
    while True:
        if(temperatura == -1):
            temperatura = random.uniform(-5.00, 90.0) # Obtiene un valor inicial de temperatura
        temperatura += random.normalvariate(0.00, 2.00) # Varia la temperatura
        temperatura = round(temperatura, 2)
        payload = str(temperatura)+" °C"
        pub.publicar(con.TOPIC_GENERAL_ALL,payload)
        time.sleep(2)
except KeyboardInterrupt:
    pub.desconectar()