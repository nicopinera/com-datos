import paho.mqtt.client as mqtt
import config as con
# Parametros de coneccion

#Callback
def on_connect(client, userdata, flag, rc):
    print("Conectado al broker mqtt desde mosquitto ")
    mensaje = "Hola mundo bzzzz... bzzzzz... "
    client.publish(con.TOPIC_PRUEBA, mensaje)
    
# Creacion del cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect

# Coneccion al broker
client.connect(con.BROKER, con.PORT, con.TIME_TO_CONNECT)

    
try:
    #permanecer conectado
    client.loop_forever()
except KeyboardInterrupt:
    print("Desconectado del broker")
    client.loop_stop()
    client.disconnect()
    print("Dispositivo desconectado")


