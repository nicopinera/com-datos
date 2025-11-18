from pub import Subcriptor
from pub import Publicador
from datetime import datetime
from pathlib import Path
import paho.mqtt.client as mqtt
import time
import config as con
import csv

def on_message(client, userdata, msg):
    texto = msg.payload.decode() # Valor tomado
    if texto not in con.LISTA_COMANDOS:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Timestamp
        archivo = Path(con.ARCHIVO)
        escribir_header = not archivo.exists() or archivo.stat().st_size == 0
        with open(con.ARCHIVO,con.MODO, newline='') as file:
            escritor = csv.writer(file)
            if escribir_header:
                escritor.writerow(["timestamp","topic", "dato"])
            escritor.writerow([timestamp,msg.topic, texto])

gateway = Subcriptor(con.TOPIC_ALL,nombre="Gateway General")
gateway.conectar(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
gateway.cliente.on_message = on_message
gateway.cliente.loop_start()

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
