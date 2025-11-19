from pub import Subcriptor
from pub import Publicador
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
import sqlite3
import paho.mqtt.client as mqtt
import time
import config as con
import csv

def imprimir_datos_db():
    conexion = sqlite3.connect(con.DB)  # Conectar a la base de datos
    cursor = conexion.cursor()  # Crear un cursor para ejecutar consultas
    temp_sala1 = [] # Guarda los valores de temperatura para la sala 1
    temp_sala2 = [] # Guarda los valores de temperatura para la sala 2
    hum_sala1 = [] # Guarda los valores de humedad para la sala 1
    hum_sala2 = [] # Guarda los valores de humedad para la sala 2
    try:
        cursor.execute("SELECT sala, sensor, valor_C FROM datos")
        filas = cursor.fetchall()  # Obtener todas las filas de la consulta

        if filas:
            print("Datos en la base de datos:")
            for fila in filas:
                sala = fila[0]
                sensor = fila[1]
                valor = fila[2]
                if sala == "sala1" and sensor == "temp":
                    temp_sala1.append(valor)
                elif sala == "sala1" and sensor == "hum":
                    hum_sala1.append(valor)
                elif sala == "sala2" and sensor == "temp":
                    temp_sala2.append(valor)
                elif sala == "sala2" and sensor == "hum":
                    hum_sala2.append(valor)
                # print(f"Sala: {fila[0]}, Sensor: {fila[1]}, Valor: {fila[2]}")
            fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 filas, 2 columnas

            # Subplot 1: Temperatura Sala 1
            axs[0, 0].plot(temp_sala1, marker='o', linestyle='-', color='b')
            axs[0, 0].set_title("Temperatura Sala 1")
            axs[0, 0].set_xlabel("Medición")
            axs[0, 0].set_ylabel("Valor [°C]")
            axs[0, 0].grid()

            # Subplot 2: Humedad Sala 1
            axs[0, 1].plot(hum_sala1, marker='o', linestyle='-', color='g')
            axs[0, 1].set_title("Humedad Sala 1")
            axs[0, 1].set_xlabel("Medición")
            axs[0, 1].set_ylabel("Valor [%]")
            axs[0, 1].grid()

            # Subplot 3: Temperatura Sala 2
            axs[1, 0].plot(temp_sala2, marker='o', linestyle='-', color='r')
            axs[1, 0].set_title("Temperatura Sala 2")
            axs[1, 0].set_xlabel("Medición")
            axs[1, 0].set_ylabel("Valor [°C]")
            axs[1, 0].grid()

            # Subplot 4: Humedad Sala 2
            axs[1, 1].plot(hum_sala2, marker='o', linestyle='-', color='m')
            axs[1, 1].set_title("Humedad Sala 2")
            axs[1, 1].set_xlabel("Medición")
            axs[1, 1].set_ylabel("Valor [%]")
            axs[1, 1].grid()

            # Ajustar el diseño
            plt.tight_layout()
            plt.show()
        else:
            print("La base de datos está vacía.")
    except sqlite3.OperationalError as e:
        print(f"Error al acceder a la base de datos: {e}")
    finally:
        conexion.close()  # Cerrar la conexión

def parceo_string(topic:str,texto:str):
    sala = ""
    sensor = ""
    valor = 0
    lista_topic = topic.split('/') # Genero una lista de los string separados por /
    lista_valor = texto.split(' ') #10.5 °C
    valor = float(lista_valor[0])
    sala = lista_topic[1] # salaX
    sensor = lista_topic[3] #hum - temp
    return sala,sensor,valor

def on_connect(client, userdata, flag, rc):
    print("Conectado al broker mqtt desde mosquitto ")
    print(f"Intentando conectarse al topico...")
    client.subscribe(con.TOPIC_ALL)
    print(f"Suscrito a {con.TOPIC_ALL}")
    print("Creando base de datos")
    conexion = sqlite3.connect(con.DB)
    try:
        conexion.execute("""
            create table datos (
                         mes integer,
                         dia integer,
                         sala text,
                         sensor text,
                         valor_C real
                         )
        """)
        print("Se creo la tabla de datos")
    except sqlite3.OperationalError:
        print("La tabla de datos ya existe")
        conexion.close()

# Funcion para crear el csv
def on_message(client, userdata, msg):
    texto = msg.payload.decode() # Valor tomado
    conexion = sqlite3.connect(con.DB) # conexion a la base de datos

    # Ignorar los comandos
    if texto not in con.LISTA_COMANDOS:
        sala,sensor,valor = parceo_string(msg.topic,texto)
        timestamp = datetime.now().strftime('%H:%M:%S') # Timestamp para el CSV
        timestamp_db = datetime.now().strftime("%m-%d") # Timestamp para la base de datos
        fecha = timestamp_db.split('-')
        mes = int(fecha[0])
        dia = int(fecha[1])
        conexion.execute("insert into datos(mes,dia,sala,sensor,valor_C) values (?,?,?,?,?)",(mes,dia,sala,sensor,valor))
        conexion.commit()
        archivo = Path(con.ARCHIVO)
        escribir_header = not archivo.exists() or archivo.stat().st_size == 0 # Escribir encabezado del CSV

        with open(con.ARCHIVO,con.MODO, newline='') as file:
            escritor = csv.writer(file)
            if escribir_header:
                escritor.writerow(["timestamp","topic", "dato"])
            escritor.writerow([timestamp,msg.topic, texto])
    conexion.close()

# Creacion del gateway
gateway = Subcriptor(con.TOPIC_ALL,nombre="Gateway General")
gateway.conectar(con.BROKER,con.PORT,con.TIME_TO_CONNECT)
gateway.cliente.on_connect = on_connect
gateway.cliente.on_message = on_message
gateway.cliente.loop_start()

# Creacion del publicador de comandos
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
    imprimir_datos_db()
