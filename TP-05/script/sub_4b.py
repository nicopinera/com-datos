from pub import Subcriptor
import paho.mqtt.client as mqtt
import time
import config as con

# Configurar 2 o mas clientes para sub a Topic Broadcast
lista_sub = []

for i in range(2):
    sub = Subcriptor(con.TOPIC_GENERAL,nombre=f"Sub{i+1}")
    sub.conectar(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
    sub.cliente.loop_start()
    lista_sub.append(sub)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    for s in lista_sub:
        s.desconectar()