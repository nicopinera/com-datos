import paho.mqtt.client as mqtt
import random
import time
import config as con
import datetime

#Dispositivo A
#Callback   
def on_connect(client, userdata, flag, rc):
    print("Conectado al broker mqtt desde mosquitto ")

dispositivoA = mqtt.Client()
dispositivoA.on_connect = on_connect

dispositivoA.connect(con.BROKER, con.PORT, con.TIME_TO_CONNECT)

dispositivoA.loop_start()


try:
    temperatura = 9999
    while True:
        if(temperatura == 9999):
            temperatura = random.uniform(-5.00, 90.0) # Obtiene un valor inicial de temperatura
        temperatura += random.normalvariate(0.00, 2.00) # Varia la temperatura
        temperatura = round(temperatura, 2)
        payload = str(temperatura)+" °C"
        dispositivoA.publish(con.TOPIC_DEVA, payload)
        time.sleep(10.0)
except KeyboardInterrupt:
    print("Desconectado del broker")
    dispositivoA.loop_stop()
    dispositivoA.disconnect()
    print("Dispositivo desconectado")

