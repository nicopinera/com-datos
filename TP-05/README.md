# Trabajo Práctico N°5: Capa de acceso en redes locales, protocolos y fundamentos

## Nombres

- Nicolás Piñera
- Julián Krede
- Noelia Valarezo

**Nombre del grupo**: Puerto1337

## UNC - Facultad de Ciencias Exactas, Físicas y Naturales

## Cátedra: Comunicaciones de Datos

### Profesores

- Henn, Santiago Martín

- Oliva Cuneo, Facundo

- Solinas, Miguel Ángel

**Fecha:**

---

## Información de los autores

- **Información de contacto**:

  - [nicolas.pinera@mi.unc.edu.ar](mailto:nicolas.pinera@mi.unc.edu.ar)
  - [julian.krede@mi.unc.edu.ar](mailto:julian.krede@mi.unc.edu.ar)
  - [noelia.valarezo@mi.unc.edu.ar](mailto:noelia.valarezo@mi.unc.edu.ar)

---

## Resumen

En este trabajo práctico se explora el protocolo MQTT, un estándar de mensajería ampliamente utilizado en el Internet de las Cosas (IoT). Se analizan sus características, ventajas, desventajas y aplicaciones principales. Además, se implementan diferentes scripts en Python para simular escenarios de publicación y suscripción, incluyendo la generación de métricas de sensores y su almacenamiento en un archivo CSV. Finalmente, se discuten las limitaciones del protocolo en redes LAN y su dependencia de un Broker central.

**Palabras clave**: MQTT, IoT, Publicación/Suscripción, Broker, Sensores, Redes LAN.

---

## Introducción

El protocolo MQTT (Message Queuing Telemetry Transport) es un estándar de mensajería ligero diseñado para dispositivos con recursos limitados y redes con ancho de banda reducido. Su arquitectura basada en el modelo de publicación/suscripción lo hace ideal para aplicaciones IoT, donde la eficiencia y la escalabilidad son esenciales. Este trabajo práctico tiene como objetivo explorar las características del protocolo, implementar casos de uso prácticos y analizar sus ventajas y limitaciones en el contexto de redes locales.

---

## Resultados

### Consigna 1

**MQTT (Message Queuing Telemetry Transport)** es un protocolo de mensajería estándar OASIS para el Internet de las Cosas (IoT). Está diseñado como un protocolo de mensajería de *publicación/suscripción* extremadamente ligero, ideal para conectar dispositivos remotos de recursos limitados, con un código de tamaño reducido y un ancho de banda de red mínimo. En la actualidad, MQTT se utiliza en una amplia variedad de sectores, pero es muy utilizado para conectar dispositivos de IoT, ya que resulta fácil de implementar y puede comunicar datos de manera eficiente.

#### Historia sobre la creación de MQTT

El protocolo MQTT se inventó en 1999 para su uso en la industria del petróleo y el gas. Los ingenieros necesitaban un protocolo para un ancho de banda y una pérdida de batería mínima para supervisar los oleoductos vía satélite. Inicialmente, el protocolo se conocía como transporte de telemetría de Message Queue Server debido al producto de IBM MQ Series que admitió por primera vez su fase inicial. En 2010, IBM lanzó MQTT 3.1 como un protocolo gratuito y abierto para que cualquiera pudiera implementarlo, que después, en 2013, se envió al organismo de especificación de la Organización para el Avance de Estándares de Información Estructurada (OASIS) para su mantenimiento. En 2019, OASIS lanzó una versión 5 de MQTT actualizada.

#### Ventajas

- *Ligero y eficiente*: Este protocolo fue concebido para enlaces satelitales de pago por byte, lo que hace que el overhead se vuelva significativo cuando el cuerpo del mensaje es pequeño, ya que tiene solo 2 bytes fijos.

- *Baja demanda de energía*: Su diseño optimizado para transferencias de datos cortas y eficientes permite que los dispositivos operen con menor consumo de energía.

- *Escalable*: Tiene funciones integradas para admitir la comunicación con una gran cantidad de dispositivos IoT.

- *Soporta TCP/IP*: Por lo tanto, puede correr sobre distintos medios físicos o tecnologías de red: Wi-Fi, Ethernet, 4G, 5G, LoRaWAN, etc.

- *Fiable*: Tiene reconexión automática, mantiene el estado del cliente y ofrece 3 niveles de QoS que permiten garantizar la entrega, incluso bajo mala conectividad.

- *Calidad de Servicio (QoS)*: Define tres niveles de garantía de entrega de mensajes:
  - *QoS 0 (Como mucho una vez entrega)*: El mensaje se envía una vez sin confirmación. No hay garantía de llegada. Adecuado si la pérdida de datos es aceptable. Requiere la menor cantidad de tráfico de red y es perfecto para proyectos de smart-home.
  - *QoS 1 (Al menos una vez entrega)*: El mensaje se garantiza que llega al menos una vez. Se utiliza si la entrega de mensajes necesita ser garantizada, pero se permiten duplicados.
  - *QoS 2 (Exactamente una vez entrega)*: El mensaje se garantiza que llega exactamente una vez (el nivel más seguro, pero más lento).

- *Seguro*: Permite el cifrado de mensajes y la autenticación de dispositivos y usuarios mediante protocolos de autenticación modernos.

- *Soportado en varios lenguajes de programación*: Java, Python, C/C++, JavaScript, C# y PHP.

#### Desventajas

- *Modelo PUB/SUB rígido*: No permite configuraciones mesh o peer-to-peer.

- *Dependencia total de un nodo central (broker)*:
  - No existe la comunicación cliente-cliente.
  - Único punto de fallo: si el broker cae, todo el sistema se detiene.

- *No tiene descubrimiento automático ni negociación de capacidades*: Todo debe configurarse manualmente o vía otra capa.

#### Principales Usos

- *Internet de las Cosas (IoT)*: Recolección de datos de sensores remotos, control de dispositivos inteligentes.
- *Sistemas de Telemetría*: Monitoreo remoto de vehículos, maquinaria o procesos industriales (IIoT).
- *Aplicaciones Móviles*: Notificaciones push y aplicaciones de mensajería que requieren bajo consumo de batería.
- *Redes con Recursos Limitados*: Comunicaciones por satélite o en áreas con poca cobertura.

#### Patrón de arquitectura Pub/Sub

El modelo **Publish/Subscribe (Pub/Sub)** es un patrón de diseño en el cual los componentes que producen información (*publishers*) y los que la consumen (*subscribers*) están desacoplados entre sí por medio de un componente (*Broker*) que actúa como intermediario. La responsabilidad del broker es recibir los mensajes que publican los publishers, clasificarlos según su tema correspondiente y distribuirlos a todos los receptores interesados en ese tema. Esta intermediación elimina la necesidad de que publishers y subscribers interactúen directamente, lo que produce un desacoplamiento tanto espacial como temporal.

![Modelo pub/sub](https://github.com/user-attachments/assets/edcc88ec-f5a9-47ea-81aa-fc8cfd7d0adb)

---

### Consigna 2

Para la realización de nuestro trabajo práctico optamos por usar el broker Mosquitto en Python, dado que es de código abierto y sencillo de utilizar.

![Envío de datos](https://github.com/user-attachments/assets/3ce4e696-bd74-448d-8762-fe9d271a57c8)

---

### Consigna 3

Para empezar, se desarrolló una clase publicador y otra suscriptor para simplificar el desarrollo de la experiencia. La implementación de las clases se encuentra en el script [pub.py](/TP-05/script/pub.py). Luego se envió un mensaje de "Hola Mundo" mediante el script [pub_hello_world.py](/TP-05/script/pub_hello_world.py).

![Envío de datos](https://github.com/user-attachments/assets/a25b0ae8-658a-4b6b-9bba-1c29739c8dc7)

Mediante el comando `mosquitto_sub -t "#" -v` se pueden ver los mensajes de todos los tópicos y con la opción `-v` se configura para que se muestre el tópico al cual corresponde cada mensaje.

![Recepción desde el broker](https://github.com/user-attachments/assets/fa773ccb-5f3e-40db-92e1-079343143778)

Para poder realizar esto de manera simple, se generó un [Makefile](/TP-05/Makefile) con diferentes steps, que se pueden utilizar para instalar el cliente, verificar el estado, e instalar las dependencias de Python. Los comandos útiles son:

```bash
make install_mosquitto # Instala el cliente Mosquitto
make start_mosquitto # Inicia el servicio y verifica el estado
make python # Genera un entorno virtual e instala los requerimientos
make terminal_holaMundo # Ver mensaje de tópico
make terminal # Ver mensaje de tópico
make terminal_pub # Ver mensaje de tópico
```

---

### Consigna 4

Para esta consigna simulamos al publicador en el script [publisher_4a.py](/TP-05/script/publisher_4a.py), el cual es un sensor de temperatura que publica sus datos cada 3 segundos. Estas métricas son publicadas en el tópico *lan/device/status*. Todos los parámetros de configuración se encuentran en [config.py](/TP-05/script/config.py).

![sub de status](https://github.com/user-attachments/assets/10ba27c3-9c2e-4e37-970d-75093173a608)

Luego, el suscriptor implementado mediante el script [suscriber_4a.py](/TP-05/script/suscriber_4a.py) recibe las métricas y las imprime para que sean visibles por pantalla.

![pub de status](https://github.com/user-attachments/assets/ab041825-bd4e-4f7d-b278-b22ce9ed94e7)

Para generar un grupo de suscriptores al tópico **lan/broadcast/#** utilizamos el script [sub_4b.py](/TP-05/script/sub_4b.py), en el cual generamos una lista de la clase Subscriptor. A todos los identificamos con un nombre y les pasamos dicho tópico. Para la creación del Publicador se utilizó el script [pub_4b.py](/TP-05/script/pub_4b.py), en el cual se crea un único publicador que enviará la información al tópico **lan/broadcast/all**. A continuación, se presenta el resultado obtenido:

![Sub-Pub-4b](https://github.com/user-attachments/assets/f73d1182-eb31-4c96-b83d-11eb91bd6f44)

---

### Consigna 5

Para esta consigna, en el script [pub_5.py](/TP-05/script/pub_5.py) simulamos un grupo de 4 sensores (2 de temperatura y 2 de humedad), los cuales cada 1 segundo generan un valor aleatorio de la cantidad sensada, y lo publican en el broker. Cada uno tiene su determinado **tópico**. Dentro del mismo script se genera una función `on_message` para asignarle al suscriptor del **tópico** destinado a los comandos. Se termina de generar una lista para los publicadores disponibles, se les asignan todos los valores necesarios para la conexión. Por último, se crea un suscriptor al **tópico: lan/comandos** para recibir los comandos **START** y **STOP**, los cuales dan inicio o detienen la simulación respectivamente.

Dentro del script [sub_5.py](/TP-05/script/sub_5.py) generamos:

- El gateway: definimos la función `on_connect`, la cual se suscribe al **tópico: lan/#** y genera la base de datos que almacena el mes y día cuando se generó el valor sensado, la sala y el sensor de la misma, y el valor obtenido.

- La función `on_message` para que el suscriptor se conecte a la base de datos y guarde los valores obtenidos con su respectivo formato. Además, genera un archivo .csv. Tanto la base de datos como el archivo .csv están en [datos](/TP-05/datos/).

- La función auxiliar `parceo_string` nos devuelve los valores de la sala, sensor y valor obtenidos en el mensaje. Y la función `imprimir_datos` nos genera un gráfico de los valores obtenidos por los 4 sensores.

A continuación, se presentan tres imágenes: en la primera se ve el funcionamiento de los scripts, en la segunda el archivo .csv con los datos almacenados, y en la última el gráfico obtenido.

![Ejemplo_uso](https://github.com/user-attachments/assets/01bcf3ff-c98c-4c0b-a262-edc01414e36d)

![Datos_csv](https://github.com/user-attachments/assets/9c0cb5f3-50f1-402d-8a69-9a3212c69b8d)

![Gráfica_datos](https://github.com/user-attachments/assets/eda892ee-9516-4d25-80de-93dfb25977a7)

> [!NOTE]
> Falta lo del sniffer.

El protocolo **MQTT** está diseñado y se implementa fundamentalmente sobre el protocolo **TCP**. TCP, al ser un protocolo orientado a la conexión y fiable, es utilizado por MQTT para garantizar una sesión persistente y una entrega ordenada y verificada de los paquetes entre los clientes y el Broker.

> [!NOTE]
> Falta respuesta B.

Los niveles de Calidad de Servicio (QoS) en MQTT son el mecanismo primario para asegurar la fiabilidad en la entrega de mensajes. Estos niveles definen el grado de garantía de que un mensaje será entregado y recibido por el suscriptor (o el Broker). La elección del nivel de QoS impacta directamente el equilibrio entre la velocidad de la comunicación y la garantía de que los datos de los sensores serán recibidos.

El modelo Pub/Sub ofrece ventajas significativas sobre el modelo tradicional Cliente-Servidor en esta arquitectura de IoT:

- **Desacoplamiento**: Los publicadores y suscriptores están desacoplados en el espacio y el tiempo. Los sensores envían datos a un tópico sin necesidad de conocer la identidad o ubicación de los consumidores.

- **Escalabilidad**: Permite una comunicación uno a muchos eficiente. Un sensor publica un mensaje una sola vez al Broker, y el Broker se encarga de distribuirlo a los suscriptores interesados, minimizando la carga en el dispositivo publicador.

- **Eficiencia**: MQTT es ligero y eficiente en ancho de banda, lo que lo hace ideal para dispositivos con recursos limitados, en contraste con la sobrecarga de cabecera que a menudo tienen los protocolos basados en Cliente-Servidor, como HTTP.

A pesar de su eficiencia para la mensajería, MQTT presenta limitaciones en el contexto de una red LAN completa:

- **Alcance de Protocolo**: MQTT es un protocolo de capa de aplicación para mensajería y no reemplaza los protocolos fundamentales de red de una LAN (como DHCP, DNS o enrutamiento IP), los cuales son necesarios para que la comunicación exista.

- **Dependencia del Broker**: Toda la comunicación entre los dispositivos debe pasar por el Broker central. Una LAN real permite comunicación peer-to-peer directa (sin intermediarios) utilizando protocolos subyacentes como TCP/IP o UDP.

- **Transferencia de Archivos Grandes**: MQTT está optimizado para la transferencia eficiente de mensajes pequeños de telemetría. Para la transferencia de grandes volúmenes de datos o archivos (como actualizaciones de firmware o logs de alta resolución), protocolos como HTTP o FTP suelen ser más adecuados y eficientes.

La dependencia de un Broker central introduce dos implicaciones operativas críticas:

- **Punto Único de Fallo (SPOF)**: La operatividad del Broker es esencial para todo el sistema. Si el Broker deja de funcionar, toda la comunicación se paraliza: los sensores no pueden enviar datos y los comandos de control no pueden ser distribuidos, resultando en una interrupción completa del servicio.

- **Cuello de Botella y Latencia**: A medida que la red escala (aumentando el número de clientes o el volumen de mensajes), el Broker puede convertirse en un cuello de botella de rendimiento. La necesidad de que cada mensaje se procese en el Broker antes de ser reenviado también introduce una pequeña latencia inherente a la comunicación indirecta.

---

## Discusión y conclusiones

El protocolo MQTT se presenta como una solución eficiente y escalable para la comunicación en entornos IoT, gracias a su diseño ligero y su modelo de publicación/suscripción. Sin embargo, su dependencia de un Broker central introduce desafíos como el punto único de fallo y posibles cuellos de botella en redes de gran escala. A pesar de estas limitaciones, MQTT sigue siendo una herramienta poderosa para aplicaciones donde la simplicidad y la eficiencia son prioritarias. En redes LAN, su uso debe complementarse con otros protocolos para cubrir aspectos como la comunicación peer-to-peer y la transferencia de datos de mayor volumen.

---

## Referencias

[1] [Página oficial de MQTT](https://mqtt.org/)

[2] [AWS Sobre MQTT](https://aws.amazon.com/es/what-is/mqtt/)

[3] [MQTT](https://www.nabto.com/mqtt-protocol-iot/)
