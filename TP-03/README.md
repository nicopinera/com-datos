# Trabajo Practico N3

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

## Resultados

### Consigna 1

Tanto el 802.3 como el 802.11 son ramas de la familia IEEE 802, un conjunto de estándares que empezó a desarrollarse en febrero de 1980 (de ahí el “802”) por el IEEE (Institute of Electrical and Electronics Engineers).

En los años 70 y principios de los 80, las computadoras empezaban a dejar de estar aisladas. Se multiplicaban en oficinas, universidades y empresas, y surgía la necesidad de que compartieran datos: impresoras, discos, correo electrónico interno.

El IEEE 802 nace en 1980 para resolver esa fragmentación. El objetivo era definir estándares abiertos para redes de área local (LAN) y de área metropolitana (MAN) que cualquiera pudiera implementar, garantizando interoperabilidad entre equipos de distintos fabricantes.

El estándar 802.3 se aprobó en 1983, tomando como base la tecnología Ethernet creada por empresas como Xerox, DEC e Intel en los años 70. Este estandar define la capa física y la subcapa MAC de redes LAN cableadas.

El primer estándar 802.11 se aprobó en 1997, con velocidades de apenas 2 Mbps. Este estandar define las LAN inalámbricas (WLAN), también en capas física y la subcapa MAC.

#### Determinacion del protocolo usado por la red de la facultad

*Pendiente*

Si una red Wi-Fi opera con un protocolo que la NIC de la notebook vieja no soporta, el resultado depende de si existe algún estándar en común entre ambos:

- Si comparten al menos un estándar y el access point esta en modo mixto: La conexión se establece usando ese estándar compartido. Como consecuencia el dispositivo funciona, pero a menor velocidad y con posibles penalizaciones de eficiencia en la red.

- Si no comparten ningún estándar: La notebook simplemente no logra conectarse, inclusive la red puede ni siquiera aparecer en la lista, o la asociación fallará siempre.

La versión del protocolo Wi-Fi no incluye directamente la seguridad de la red, las distintas versiones que se lanzan de 802.11 define velocidad, modulación, técnicas de transmisión. La seguridad en Wi-Fi está definida por extensiones de 802.11 (WEP, WPA, WPA2, WPA3), que van evolucionando en paralelo a las versiones del estandar 802.11, cada nueva generación trae consigo recomendaciones mínimas de seguridad.

En resumen se podria decir que la relación es indirecta: Las versiones modernas del estandar suelen desplegarse junto con sistemas de seguridad más recientes (WPA2, WPA3).

*pendiente revisar la seguridad que tiene la red de la facu*

#### Tabla comparativa de los protocolos mas recientes

|                        | Wi-Fi 5       | Wi-Fi 6        | Wi-Fi 7        |
|------------------------|---------------|----------------|----------------|
| Versión IEEE           | 802.11ac      | 802.11ax       | 802.11be       |
| Tasa de datos máxima   | ~3.5 Gbps     | ~9.6 Gbps      | ~30 Gbps       |
| Banda(s)               | 5 GHz         | 2.4 GHz / 5 GHz / 6 GHz (para Wi-Fi 6E) | 2.4 GHz / 5 GHz / 6 GHz |
| Ancho de Banda         | 20/40/80/160 MHz | 20/40/80/160 MHz | 20/40/80/160/320 MHz |
| Modulación             | 256-QAM       | 1024-QAM       | 4096-QAM       |
| Sistema de Seguridad   | WPA2/WPA3     | WPA3           | WPA3           |

---

### Consigna 2

![Fibra optica monomodo y multimodo](/img/fibra-optica-modos.png)

En el lado izquierdo tenemos la fibra óptica monomodo, la cual está diseñada para que la luz viaje por un solo modo o trayectoria dentro de su núcleo muy delgado, de aproximadamente 8 a 10 micrómetros. Esto le permite transmitir datos a muy largas distancias con un ancho de banda muy alto y con mínima dispersión. \
Sin embargo, requiere láseres precisos para emitir la luz y su implementación es bastante más costosa, tanto por la fibra como por los equipos asociados. Es la opción que se suele usar en redes troncales y telecomunicaciones de larga distancia.

En lado derecho tenemos la fibra óptica multimodo, que permite que la luz se propague por varios modos simultáneamente gracias a un núcleo más ancho, de entre 50 y 62,5 micrómetros. Esto hace que sea más fácil de fabricar y que funcione con LEDs menos precisos, pero limita la distancia de transmisión y el ancho de banda debido a la dispersión modal. Su implementación es más económica y se utiliza principalmente en redes locales, centros de datos y conexiones de corta distancia.

Nota: Cuando hablamos de “modos” en fibra óptica, nos referimos a las posibles trayectorias o caminos que la luz puede seguir dentro del núcleo de la fibra mientras se propaga.

#### Ley de Snell

Recordando la ley de Snell:

$$n_1 \cdot \sin{\theta_1} = n_2 \cdot \sin{\theta_2}$$

Donde:\
$n_1,n_2$: Índices de refracción de los dos medios.

$\theta_1$: Ángulo de incidencia de la luz respecto a la normal.

$\theta_2$: Ángulo de refracción dentro del segundo medio.

En la fibra óptica, el núcleo tiene un índice de refracción ligeramente mayor que el revestimiento que lo rodea. Gracias a esto, si la luz entra al núcleo con un ángulo adecuado, en lugar de salir al revestimiento, se refleja completamente dentro del núcleo, fenómeno que se llama reflexión total interna.

Esta relación con la Ley de Snell también explica los distintos modos de transmisión. En una fibra monomodo, el núcleo es tan delgado que solo existe un ángulo que cumple la condición de reflexión total interna, por eso la luz sigue una sola trayectoria. En cambio, en una fibra multimodo, el núcleo más ancho permite que la luz entre en varios ángulos distintos, cada uno cumpliendo la Ley de Snell, generando múltiples trayectorias o modos.

Aunque a primera vista las conexiones inalámbricas y la fibra óptica parecen tecnologías totalmente distintas, en realidad están estrechamente relacionadas. La fibra óptica transmite datos mediante luz guiada (que no es otra cosa que una onda electromagnetica) por un medio físico, mientras que las conexiones inalámbricas lo hacen mediante ondas electromagnéticas que viajan por el aire. En ambos casos, el objetivo es transportar información de un punto a otro, y ambos deben lidiar con la forma en la que se propagan esas ondas para que la señal llegue correctamente.

En la fibra, la luz se mantiene dentro del núcleo gracias a la reflexión total interna, mientras que en el aire las ondas pueden rebotar, refractarse o perderse en obstáculos; aun así, en ambos casos el control de la propagación es clave para la eficiencia de la transmisión. Además, la fibra óptica ofrece un ancho de banda y velocidad mucho mayores que el inalámbrico, lo que hace que muchas redes combinen ambas tecnologías: la fibra actúa como la columna vertebral de la red, transportando grandes volúmenes de datos a alta velocidad, y el acceso inalámbrico permite la conexión flexible y móvil de los usuarios finales.

---

## Discusión y conclusiones

---

## Referencias

[1] [TechTarget - IEEE 802 Wireless Standards Reference](https://www.techtarget.com/searchnetworking/reference/IEEE-802-Wireless-Standards-Fast-Reference)

[2] [Copperpod - A Comprehensive Comparison of Wi-Fi 5, 6, and 7](https://www.copperpodip.com/post/demystifying-wi-fi-a-comprehensive-comparison-of-wi-fi-5-6-and-7#:~:text=Conclusi%C3%B3n,y%20capaz%20hasta%20la%20fecha.)

[3] [Patch Box Blog - Fibra optica monomodo y multimodo](https://patchbox.com/es/blog/monomodo-multimodo-fibra-optica/)

[4] []()

[5] []()
