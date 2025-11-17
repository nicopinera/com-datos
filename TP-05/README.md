# Trabajo Practico N5 : Capa de acceso en redes locales, protocolos y fundamentos

## Nombres

- Nicolas Piñera
- Julian Krede
- Noelia Valarezo

**Nombre del grupo**: Puerto1337

## UNC - Facultad de Ciencias Exactas, Físicas y Naturales

## Cátedra: Comunicaciones de Datos

### Profesores

- Henn, Santiago Martin

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

**Palabras clave**:

---

## Introducción

---

## Resultados

### Consigna 1

**MQTT (Message Queuing Telemetry Transport)** es un protocolo de mensajería estándar OASIS para el Internet de las cosas (IoT). Está diseñado como un protocolo de mensajería de *publicación/suscripción* extremadamente ligero, ideal para conectar dispositivos remotos de recursos limitados, con un código de tamaño reducido y un ancho de banda de red mínimo. En la actualidad, MQTT se utiliza en una amplia variedad de sectores, pero es muy utilizando para conectar dispositivos de IoT, ya que resulta fácil de implementar y puede comunicar datos de manera eficiente.

#### Historia sobre la creacion de MQTT

El protocolo MQTT se inventó en 1999 para su uso en la industria del petróleo y el gas. Los ingenieros necesitaban un protocolo para un ancho de banda y una pérdida de batería mínima para supervisar los oleoductos vía satélite. Inicialmente, el protocolo se conocía como transporte de telemetría de Message Queue Server debido al producto de IBM MQ Series que admitió por primera vez su fase inicial. En 2010, IBM lanzó MQTT 3.1 como un protocolo gratuito y abierto para que cualquiera pudiera implementarlo, que después, en 2013, se envió al organismo de especificación de la Organización para el Avance de Estándares de Información Estructurada (OASIS) para su mantenimiento. En 2019, OASIS lanzó una versión 5 de MQTT actualizada.

#### Ventajas

- *Ligero y eficiente*: Este protocolo fue concebido para enlaces satelitales de pago por byte, esto hace que el overhead se vuelve significativo cuando el cuerpo del mensaje es pequeño, tiene solo 2 bytes fijos.

- *Baja Demanda de Energía*: Su diseño optimizado para transferencias de datos cortas y eficientes permite que los dispositivos operen con menor consumo de energía.

- *Escalable*: Tiene funciones integradas para admitir la comunicación con una gran cantidad de dispositivos IoT.

- *Soporta TCP/IP*: Por lo tanto, puede correr sobre distintos medios físicos o tecnologías de red: Wi-Fi, Ethernet, 4G, 5G, LoRaWAN, etc

- *Fiable*: Tiene reconexión automática, mantiene estado del cliente y ofrece 3 niveles de QoS que permiten garantizar entrega, incluso bajo mala conectividad.

- *Calidad de Servicio (QoS)*: Define tres niveles de garantía de entrega de mensajes:
  - *QoS 0 (Como mucho una vez entrega)*: El mensaje se envía una vez sin confirmación. No hay garantía de llegada. Adecuado si la pérdida de datos es aceptable. Requiere la menor cantidad de tráfico de red y es perfecto para proyectos de smart-home.
  - *QoS 1 (Al menos una vez entrega)*: El mensaje se garantiza que llega al menos una vez. Se utiliza si la entrega de mensajes necesita ser garantizada, pero se permiten duplicados.
  - *QoS 2 (Exactamente una vez entrega)*: El mensaje se garantiza que llega exactamente una vez (el nivel más seguro, pero más lento).

- *Seguro*: Permite el cifrado de mensajes y la autenticación de dispositivos y usuarios mediante protocolos de autenticación modernos

- *Soportado en varios lenguajes de programacion*: Java, Python, C/C++, JavaScript, C# y PHP

#### Desventajas

- *Modelo PUB/SUB rígido*: No permite configuraciones mesh o peer-to-peer.

- *Dependencia total de un nodo central (broker)*:
  - No existe la comunicacion cliente-cliente
  - Unico punto de fallo, si el broker cae, todo el sistema se detiene.

- *No tiene descubrimiento automático ni negociación de capacidades*: Todo debe configurarse manualmente o vía otra capa.

#### Principales Usos

- *Internet de las Cosas (IoT)*: Recolección de datos de sensores remotos, control de dispositivos inteligentes.
- *Sistemas de Telemetría*: Monitoreo remoto de vehículos, maquinaria o procesos industriales (IIoT).
- *Aplicaciones Móviles*: Notificaciones push y aplicaciones de mensajería que requieren bajo consumo de batería.
- *Redes con Recursos Limitados*: Comunicaciones por satélite o en áreas con poca cobertura.

#### Patron de arquitectura Pub/Sub

El modelo **Publish/Subscribe (Pub/Sub)** es un patron de diseño en el cual los componentes que producen información (*publishers*) y los que la consumen (*subscribers*) están desacoplados entre sí por medio de un componente (*Broker*) que actúa como intermediario. La responsabilidad del broker es recibir los mensajes que publican los publishers, clasificarlos según su tema correspondiente y distribuirlos a todos los receptores interesados en ese tema. Esta intermediación elimina la necesidad de que publishers y subscribers interactuen directamente lo que produce un desacoplamiento tanto espacial, como temporal.

![Modelo pub/sub](https://github.com/user-attachments/assets/edcc88ec-f5a9-47ea-81aa-fc8cfd7d0adb)

---

### Consigna 2

Para la realizacion de nustro trabajo practico optamos por usar el broker mosquitto en python, dado que es de codigo abierto y sencillo de utilizar

![Envio de datos](https://github.com/user-attachments/assets/3ce4e696-bd74-448d-8762-fe9d271a57c8)

---

### Consigna 3

Envio de hola mundo mediante el script `pub_hello_world.py`

![Envio de datos](https://github.com/user-attachments/assets/a25b0ae8-658a-4b6b-9bba-1c29739c8dc7)

Mediante el comando `mosquitto_sub -t "#" -v` se pueden ver los mensajes de todos los topicos y con la opcion `-v` se configura para que se muestre el topico al cual corresponde cada mensaje

![Recepcion desde el broker](https://github.com/user-attachments/assets/fa773ccb-5f3e-40db-92e1-079343143778)

Para poder realizar esto de manera simple, se genero un **Makefile** con diferentes steps, que se pueden utilizar en diferentes terminales, los cuales son:

```bash
make install_mosquitto # Instala el cliente mosquitto
make start_mosquitto # Inicia el servicio y verifica el estado
make python # Genera un entorno virtual e instala los requerimientos
make terminal_holaMundo # Ver mensaje de topico
make terminal # Ver mensaje de topico
make terminal_pub # Ver mensaje de topico
```

---

### Consigna 4

Para esta consigna mediante el script `publisher_4a.py` simulamos la obtencion de metricas de temperatura cada 3 segundos, estas metricas son publicados en el topico lan/device/status

![sub de status](https://github.com/user-attachments/assets/10ba27c3-9c2e-4e37-970d-75093173a608)

Luego el subscriber implementado mediante el script `suscriber_4a.py` recibe las metricas y las imprime para que sean visible por pantalla

![pub de status](https://github.com/user-attachments/assets/ab041825-bd4e-4f7d-b278-b22ce9ed94e7)

---

### Consigna 5

---

## Discusión y conclusiones

---

## Referencias

[1] [Pagina oficial de MQTT](https://mqtt.org/)

[2] [AWS Sobre MQTT](https://aws.amazon.com/es/what-is/mqtt/)

[3] [MQTT](https://www.nabto.com/mqtt-protocol-iot/)
