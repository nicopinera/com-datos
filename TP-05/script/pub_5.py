from pub import Publicador
import paho.mqtt.client as mqtt
import time
import config as con
import random

lista_pub = []

# Generacion de Publicadores
for i in range(4):
    pub = Publicador(f"Pub{i+1}")
    pub.connect(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
    pub.cliente.loop_start()
    lista_pub.append(pub)

try:
    while True:
        for i in range(len(lista_pub)):
            pub_actual = lista_pub[i]
            time.sleep(0.5)
        time.sleep(0.5)
except KeyboardInterrupt:
    for i in range(len(lista_pub)):
        pub_actual = lista_pub[i]
        pub_actual.desconectar()