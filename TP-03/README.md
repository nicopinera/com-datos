# Trabajo Practico N3 : Capa de acceso en redes locales, protocolos y fundamentos

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

Este informe analiza los principales estándares y tecnologías de la capa de acceso en redes locales, tanto cableadas como inalámbricas, haciendo foco en los protocolos IEEE 802.3 (Ethernet) y 802.11 (Wi-Fi), así como en los medios de transmisión como UTP, fibra óptica y tecnologías inalámbricas. Se presentan comparativas, aplicaciones prácticas y una revisión de la seguridad en redes Wi-Fi, junto con ejemplos actuales como la conectividad en aviones.

**Palabras clave**: IEEE 802.3, IEEE 802.11, Ethernet, Wi-Fi, fibra óptica, UTP, transmisión inalámbrica, seguridad, estándares, redes locales.

---

## Introducción

La comunicación de datos en redes locales es fundamental para el funcionamiento de organizaciones, instituciones educativas y hogares. Este informe aborda los conceptos y estándares clave de la capa de acceso, describiendo las tecnologías más utilizadas para la transmisión de datos, tanto por medios físicos como inalámbricos. Se analizan las características, ventajas y limitaciones de cada tecnología, así como su evolución y aplicaciones actuales, proporcionando una visión integral sobre el estado y la importancia de las redes de acceso en la actualidad.

---

## Resultados

### Consigna 1

El estándar IEEE **802.3** define el estándar **Ethernet**, el cual es la base de las redes de área local (LAN) cableadas, mientras que el IEEE **802.11** define el estándar para las redes **Wi-Fi**, que rigen las redes inalámbricas. Ambos son fundamentales para la comunicación de datos en la actualidad.

Tanto el 802.3 como el 802.11 son ramas de la familia IEEE 802, un conjunto de estándares que empezó a desarrollarse en febrero de 1980 (de ahí el “802”) por el IEEE (Institute of Electrical and Electronics Engineers).

En los años 70 y principios de los 80, las computadoras empezaban a dejar de estar aisladas. Se multiplicaban en oficinas, universidades y empresas, y surgía la necesidad de que compartieran datos: impresoras, discos, correo electrónico interno.

El IEEE 802 nace en 1980 para resolver esa fragmentación. El objetivo era definir estándares abiertos para redes de área local (LAN) y de área metropolitana (MAN) que cualquiera pudiera implementar, garantizando interoperabilidad entre equipos de distintos fabricantes.

El desarrollo de Ethernet se inició en la década de 1970 en el Xerox PARC por Robert Metcalfe. La primera especificación formal, conocida como _Ethernet Experimental_, se publicó en 1976. La IEEE adoptó el estándar en 1983, designándolo como IEEE 802.3 tomando como base la tecnología Ethernet creada por empresas como Xerox, DEC e Intel en los años 70. Este estandar define la capa física y la subcapa MAC de redes LAN cableadas.

El IEEE 802.3 se utiliza principalmente para las redes de área local (LAN) cableadas, y es el estándar dominante en hogares, oficinas, centros de datos y campus universitarios. Se usa para conectar dispositivos como computadoras de escritorio, servidores, impresoras de red y routers a través de cables de par trenzado o fibra óptica.

El desarrollo del estándar IEEE 802.11 comenzó en 1990 y la primera versión se publicó en 1997. Esta versión original tenía una velocidad máxima de 2 Mbps, lo cual era bastante lento. Las revisiones posteriores, como 802.11b, 802.11g, 802.11n, 802.11ac y 802.11ax (Wi-Fi 6), han aumentado significativamente la velocidad y mejorado la eficiencia y la seguridad. Este estandar define las LAN inalámbricas (WLAN), también en capas física y la subcapa MAC.

El IEEE 802.11 se utiliza para las redes de área local inalámbricas (WLAN). Su principal ventaja es la movilidad, permitiendo que los dispositivos como smartphones, laptops, tablets y dispositivos de IoT se conecten a la red sin necesidad de cables. Es el estándar detrás de la tecnología Wi-Fi que se encuentra en la mayoría de los lugares públicos y privados.

La red Wi-Fi de la facultad (FCEFyN 2.4GHz) utiliza el protocolo IEEE 802.11n, también conocido como Wi-Fi 4. Este estándar opera principalmente en la banda de 2.4 GHz. Puedes verificar el estándar utilizado desde la notebook accediendo a las propiedades de la red Wi-Fi conectada, donde suele aparecer el tipo de protocolo (por ejemplo, 802.11n).

> [!IMPORTANT]
> Algunas de las redes de nuestra facultad dejaron de ser libres en estos ultimos años

La capacidad de un dispositivo para conectarse a una red Wi-Fi depende directamente de la compatibilidad entre el estándar inalámbrico utilizado por el punto de acceso (router) y la tarjeta de interfaz de red (NIC) del dispositivo. Si la NIC de un equipo no es compatible con el protocolo de la red, pueden ocurrir dos escenarios principales:

- Si comparten al menos un estándar y el access point esta en **modo mixto**: El dispositivo se conectará a la red, pero su rendimiento estará limitado a la velocidad máxima del estándar más bajo. Esto puede generar una reducción de la eficiencia general de la red, ya que el punto de acceso debe destinar recursos para mantener la conexión con el dispositivo más lento, afectando potencialmente el rendimiento de los dispositivos más modernos que podrían operar a velocidades superiores.

- _Si no comparten ningún estándar_: La notebook simplemente no logra conectarse, inclusive la red puede ni siquiera aparecer en la lista, o la asociación fallará siempre.

La versión del protocolo Wi-Fi no incluye directamente la seguridad de la red, las distintas versiones que se lanzan de 802.11 define velocidad, modulación, técnicas de transmisión. La seguridad en Wi-Fi está definida por extensiones de 802.11 (WEP, WPA, WPA2, WPA3), que van evolucionando en paralelo a las versiones del estandar 802.11, cada nueva generación trae consigo recomendaciones mínimas de seguridad.

En resumen se podria decir que la relación es indirecta: Las versiones modernas del estandar suelen desplegarse junto con sistemas de seguridad más recientes (WPA2, WPA3).

Los estándares Wi-Fi 802. 11n son compatibles con los protocolos de seguridad más utilizados: WEP, WPA, WPA2 y WPA3. Sin embargo, la protección de una red no está determinada por el estandar WiFi que se implemente sino por el método de encriptación seleccionado en la configuración del enrutador. La red _FCEFyN 2.4GHz_ se considera una red abierta y, por ende, no cuenta con un protocolo de seguridad. En la informacion relacionada a la seguridad nos aparece _Ninguna/Enchanced Open_

#### Tabla comparativa de los protocolos mas recientes

|                      | Wi-Fi 5          | Wi-Fi 6                                 | Wi-Fi 7                 |
| -------------------- | ---------------- | --------------------------------------- | ----------------------- |
| Versión IEEE         | 802.11ac         | 802.11ax                                | 802.11be                |
| Tasa de datos máxima | ~3.5 Gbps        | ~9.6 Gbps                               | ~30 Gbps                |
| Banda(s)             | 5 GHz            | 2.4 GHz / 5 GHz / 6 GHz (para Wi-Fi 6E) | 2.4 GHz / 5 GHz / 6 GHz |
| Ancho de Banda       | 20/40/80/160 MHz | 20/40/80/160 MHz                        | 20/40/80/160/320 MHz    |
| Modulación           | 256-QAM          | 1024-QAM                                | 4096-QAM                |
| Sistema de Seguridad | WPA2/WPA3        | WPA3                                    | WPA3                    |

---

### Consigna 2

Las ilustraciones muestran los dos tipos principales de transmisión en fibra óptica: monomodo y multimodo.

![Image](https://github.com/user-attachments/assets/f98f53ea-cf9f-498a-970f-98b1a2b23c68)

En el lado izquierdo tenemos la fibra **óptica monomodo**, la cual está diseñada para que la luz viaje por un solo modo o trayectoria dentro de su núcleo muy delgado, de aproximadamente 8 a 10 $[\mu m]$. Esto le permite transmitir datos a muy largas distancias con un ancho de banda muy alto y con mínima dispersión.

Sin embargo, requiere láseres precisos para emitir la luz y su implementación es bastante más costosa, tanto por la fibra como por los equipos asociados. Es la opción que se suele usar en redes troncales y telecomunicaciones de larga distancia.

En lado derecho tenemos la fibra **óptica multimodo**, que permite que la luz se propague por varios modos simultáneamente gracias a un núcleo más ancho, de entre 50 y 62,5 $[\mu m]$. Esto hace que sea más fácil de fabricar y que funcione con LEDs menos precisos, pero limita la distancia de transmisión y el ancho de banda debido a la dispersión modal. Su implementación es más económica y se utiliza principalmente en redes locales, centros de datos y conexiones de corta distancia.

> [!NOTE]
> Cuando hablamos de “modos” en fibra óptica, nos referimos a las posibles trayectorias o caminos que la luz puede seguir dentro del núcleo de la fibra mientras se propaga.

#### Ley de Snell

La **Ley de Snell** es una fórmula de la óptica que describe el cambio en la dirección de un rayo de luz cuando pasa de un medio a otro con un índice de refracción diferente. El _índice de refracción_ ($n$) es una medida de la velocidad de la luz en un material; a mayor índice, menor es la velocidad de la luz.

Recordando la ley de Snell:

$$n_1 \cdot \sin{\theta_1} = n_2 \cdot \sin{\theta_2}$$

Donde:

- $n_1,n_2$: Índices de refracción de los dos medios.
- $\theta_1$: Ángulo de incidencia de la luz respecto a la normal.
- $\theta_2$: Ángulo de refracción dentro del segundo medio.

En la fibra óptica, el núcleo tiene un índice de refracción ligeramente mayor que el revestimiento que lo rodea. Gracias a esto, si la luz entra al núcleo con un ángulo adecuado, en lugar de salir al revestimiento, se refleja completamente dentro del núcleo, fenómeno que se llama **reflexión total interna**.

Esta relación con la Ley de Snell también explica los distintos modos de transmisión. En una fibra monomodo, el núcleo es tan delgado que solo existe un ángulo que cumple la condición de reflexión total interna, por eso la luz sigue una sola trayectoria. En cambio, en una fibra multimodo, el núcleo más ancho permite que la luz entre en varios ángulos distintos, cada uno cumpliendo la Ley de Snell, generando múltiples trayectorias o modos.

Aunque a primera vista las conexiones inalámbricas y la fibra óptica parecen tecnologías totalmente distintas, en realidad están estrechamente relacionadas. La fibra óptica transmite datos mediante luz guiada (que no es otra cosa que una onda electromagnetica) por un medio físico, mientras que las conexiones inalámbricas lo hacen mediante ondas electromagnéticas que viajan por el aire. En ambos casos, el objetivo es transportar información de un punto a otro, y ambos deben lidiar con la forma en la que se propagan esas ondas para que la señal llegue correctamente.

En la fibra, la luz se mantiene dentro del núcleo gracias a la reflexión total interna, mientras que en el aire las ondas pueden rebotar, refractarse o perderse en obstáculos; aun así, en ambos casos el control de la propagación es clave para la eficiencia de la transmisión. Además, la fibra óptica ofrece un ancho de banda y velocidad mucho mayores que el inalámbrico, lo que hace que muchas redes combinen ambas tecnologías: la fibra actúa como la columna vertebral de la red, transportando grandes volúmenes de datos a alta velocidad, y el acceso inalámbrico permite la conexión flexible y móvil de los usuarios finales.

### Consigna 3

A continuacion se realizara un cuadro con informacion de los estandares mas comunes

| Protocolo | Esta estandarizado? Si/No | Si corresponde: ¿Cual(es) Estandares? Mas Moderno |
| --------- | ------------------------- | ------------------------------------------------- |
| Wi-Fi     | Si                        | 802.11be (Wi-Fi 7)                                |
| Bluetooth | Si                        | Bluetooth 5.4                                     |
| ZigBee    | SI                        | ZigBee PRO 2023                                   |
| NFC       | Si                        | NFC Forum Technical Specification 2023            |
| LTE       | Si                        | LTE-Advanced                                      |
| GSM       | Si                        | No tiene una versión más moderna                  |
| 5G (3GPP) | Si                        | Release 18                                        |
| LoRa      | No                        | -                                                 |
| NB-IoT    | No                        | -                                                 |
| SigFox    | No                        | -                                                 |
| Z-Wave    | No                        | -                                                 |

De acuerdo con lo visto en clase, se completara el siguiente cuadro comparativo entre los distintos medios de transmision

| Caracteristica                           | UTP        | Fibra Optica | Wi-Fi 802.11be | Bluetooth 5.4 | 5g           |
| ---------------------------------------- | ---------- | ------------ | -------------- | ------------- | ------------ |
| Ancho de banda                           | Medio-Alto | Muy alto     | Muy alto       | Bajo          | Muy alto     |
| Distancia                                | 100 metros | varios km    | 10 m - 100 m   | 10 m - 200 m  | 1 km - 10 km |
| Inmunidad a EMI / RFI                    | Baja       | Muy alta     | Baja           | Baja          | Baja         |
| Costos de medios/conectores/dispositivos | Bajo       | Alto         | Medio          | Bajo          | Alto         |
| Disponible en Packet Tracer              | Si         | Si           | Si             | No            | No           |

### Consigna 4

Hoy en día es completamente posible conectarse a Internet en un avión en vuelo. La tecnología de conectividad a bordo, conocida como **In-Flight Connectivity (IFC)**, ha evolucionado significativamente, pasando de ser un servicio de lujo a una característica cada vez más común en las aerolíneas.

![Image](https://github.com/user-attachments/assets/d5fc3c79-6bc3-4e14-9542-0625aa8dd5ca)

Existen dos tecnologías principales que permiten la conexión a Internet en un avión: **la comunicación satelital** y **la conexión aire-tierra (Air-to-Ground)**.

1. **Comunicación Satelital (SATCOM)**: Es la tecnología más utilizada, especialmente en vuelos de larga distancia y rutas transoceánicas, ya que proporciona cobertura global. Una antena parabólica, instalada en la parte superior del fuselaje del avión, se conecta a un satélite de telecomunicaciones en órbita. Este satélite actúa como un repetidor, enviando los datos a una estación terrestre que, a su vez, los conecta a Internet. Dentro del avión, un router distribuye la señal a los dispositivos de los pasajeros a través de una red Wi-Fi.

2. **Conexión Aire-Tierra (Air-to-Ground - ATG)**: Este sistema es más común en vuelos continentales o nacionales, donde la ruta está sobre tierra firme con infraestructura de torres celulares. Funciona de manera similar a una red móvil terrestre. El avión está equipado con antenas en su parte inferior que se comunican con una red de torres de telefonía móvil terrestres optimizadas para enviar una señal ascendente. A medida que el avión se desplaza, se conecta automáticamente a la torre más cercana.

---

## Discusión y conclusiones

---

## Referencias

[1] [TechTarget - IEEE 802 Wireless Standards Reference](https://www.techtarget.com/searchnetworking/reference/IEEE-802-Wireless-Standards-Fast-Reference)

[2] [Copperpod - A Comprehensive Comparison of Wi-Fi 5, 6, and 7](https://www.copperpodip.com/post/demystifying-wi-fi-a-comprehensive-comparison-of-wi-fi-5-6-and-7#:~:text=Conclusi%C3%B3n,y%20capaz%20hasta%20la%20fecha.)

[3] [Patch Box Blog - Fibra optica monomodo y multimodo](https://patchbox.com/es/blog/monomodo-multimodo-fibra-optica/)

[4] [Noticia sobre IFC](https://aws.amazon.com/es/blogs/networking-and-content-delivery/satellite-communication-on-aws-thales-cloudifies-in-flight-wifi-service/#:~:text=Descripci%C3%B3n%20general%20del%20Wi%2DFi%20a%20bordo%20de%20Thales&text=El%20sistema%20IFC%20de%20Thales,terrestres%20en%20cada%20ubicaci%C3%B3n%20geogr%C3%A1fica.)
