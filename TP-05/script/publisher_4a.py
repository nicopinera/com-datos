import paho.mqtt.client as mqtt
import random
import time
import config as con
import datetime
from pub import Publicador


#Dispositivo A
dispositivoA = Publicador()
dispositivoA.connect(con.BROKER, con.PORT, con.TIME_TO_CONNECT)
dispositivoA.cliente.loop_start()


try:
    temperatura = 9999
    while True:
        if(temperatura == 9999):
            temperatura = random.uniform(-5.00, 90.0) # Obtiene un valor inicial de temperatura
        temperatura += random.normalvariate(0.00, 2.00) # Varia la temperatura
        temperatura = round(temperatura, 2)
        payload = str(temperatura)+" °C"
        dispositivoA.publicar(con.TOPIC_DEVA,payload)
        time.sleep(10.0)
except KeyboardInterrupt:
    print("Desconectado del broker")
    dispositivoA.desconectar()
    print("Dispositivo desconectado")

