# Broker local
BROKER = "localhost"

# Puerto
PORT = 1883

#Topic donde se envian los mensajes en el publicador de prueba
TOPIC_PRUEBA = "comDatos/TPs/TP5"

TIME_TO_CONNECT = 60 #segundos

# Topic del ejercicio 4-a
TOPIC_DEVA = "lan/deviceA/status"

# Topic General para simular broadcast 4-b
TOPIC_GENERAL = "lan/broadcast/#"
TOPIC_GENERAL_ALL = "lan/broadcast/all"

# Topic Consigna 5
TOPIC_1_TEMP = "lan/sala1/sensor/temp"
TOPIC_1_HUM = "lan/sala1/sensor/hum"
TOPIC_2_TEMP = "lan/sala2/sensor/temp"
TOPIC_2_HUM = "lan/sala2/sensor/hum"
LISTA_TOPIC_PUB = [TOPIC_1_TEMP,TOPIC_1_HUM,TOPIC_2_TEMP,TOPIC_2_HUM]