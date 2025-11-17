import paho.mqtt.client as mqtt
import config as con

# Clase publicador
class Publicador:
    def on_connect(self,client, userdata, flag, rc):
        print("Conectado al broker mqtt desde mosquitto ")
    
    def __init__(self,nombre=None):
        self.cliente = mqtt.Client()
        self.cliente.on_connect = self.on_connect
    
    def connect(self,broker,port,time_to_conect):
        self.cliente.connect(broker,port,time_to_conect)
        # self.cliente.loop_start()

    def publicar(self,topic,payload):
        self.cliente.publish(topic,payload)

    def desconectar(self):
        self.cliente.loop_stop()
        self.cliente.disconnect()

# Clase Subcriptor
class Subcriptor:
    def __init__(self):
        pass