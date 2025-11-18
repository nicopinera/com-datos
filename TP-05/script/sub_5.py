from pub import Subcriptor
from pathlib import Path
import paho.mqtt.client as mqtt
import time
import config as con
import csv

def on_message(client, userdata, msg):
    texto = msg.payload.decode() # Valor tomado
    archivo = Path(con.ARCHIVO)
    escribir_header = not archivo.exists() or archivo.stat().st_size == 0
    with open(con.ARCHIVO,con.MODO, newline='') as file:
        escritor = csv.writer(file)
        if escribir_header:
            escritor.writerow(["topic", "dato"])
        escritor.writerow([msg.topic, texto])

gateway = Subcriptor(con.TOPIC_ALL,nombre="Gateway General")
gateway.conectar(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
gateway.cliente.on_message = on_message
gateway.cliente.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    gateway.desconectar()
