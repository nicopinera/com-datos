import paho.mqtt.client as mqtt
import config as con

# Clase publicador
class Publicador:
    def on_connect(self,client, userdata, flag, rc):
        print(f"Conectado al broker mqtt desde mosquitto - Cliente{self.nombre}")
    
    def __init__(self,topic,nombre=None):
        self.topic = topic
        if(nombre != None):
            self.nombre = nombre
            self.cliente = mqtt.Client(client_id=nombre)
        else:
            self.nombre = None
            self.cliente = mqtt.Client()
        self.cliente.on_connect = self.on_connect
    
    def connect(self,broker,port,time_to_conect):
        self.cliente.connect(broker,port,time_to_conect)
        # self.cliente.loop_start()

    def publicar(self,payload):
        self.cliente.publish(self.topic,payload)

    def desconectar(self):
        self.cliente.loop_stop()
        self.cliente.disconnect()

# Clase Subcriptor
class Subcriptor:
    def on_connect(self,client, userdata, flag, rc):
        print("Conectado al broker mqtt desde mosquitto ")
        print(f"Intentando conectarse al topico...")
        client.subscribe(self.topic)
        print(f"Suscrito a {self.topic}")

    def on_message(self,client, userdata, msg):
        print(f"Mensaje recibido: {msg.payload.decode()} - Sub: {self.nombre}")

    def __init__(self,topic,nombre=None):
        self.topic = topic
        if(nombre != None):
            self.nombre = nombre
            self.cliente = mqtt.Client(client_id=nombre)
        else:
            self.cliente = mqtt.Client()
        self.cliente.on_connect = self.on_connect
        self.cliente.on_message = self.on_message
    
    def conectar(self,broker,port,time):
        self.cliente.connect(broker,port,time)
    
    def desconectar(self):
        self.cliente.loop_stop()
        self.cliente.disconnect()