import paho.mqtt.client as mqtt

# Parametros de coneccion
broker = "localhost"
port = 1883
topic = "comDatos/TPs/TP5"
time_to_connect = 60 #segundos

#Callback
def on_connect(client, userdata, flag, rc):
    print("Conectado al broker mqtt desde mosquitto ")
    mensaje = "Hola mundo bzzzz... bzzzzz... "
    client.publish(topic, mensaje)
    
    
# Creacion del cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect

# Coneccion al broker
client.connect(broker, port, time_to_connect)

#permanecer conectado
client.loop_forever()


