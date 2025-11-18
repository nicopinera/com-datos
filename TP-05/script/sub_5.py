from pub import Subcriptor
import paho.mqtt.client as mqtt
import time
import config as con

gateway = Subcriptor(con.TOPIC_ALL,nombre="Gateway General")
gateway.conectar(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
gateway.cliente.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    gateway.desconectar()
