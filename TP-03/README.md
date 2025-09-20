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

## Discusión y conclusiones

---

## Referencias

[1] [TechTarget - IEEE 802 Wireless Standards Reference](https://www.techtarget.com/searchnetworking/reference/IEEE-802-Wireless-Standards-Fast-Reference)

[2] [Copperpod - A Comprehensive Comparison of Wi-Fi 5, 6, and 7](https://www.copperpodip.com/post/demystifying-wi-fi-a-comprehensive-comparison-of-wi-fi-5-6-and-7#:~:text=Conclusi%C3%B3n,y%20capaz%20hasta%20la%20fecha.)

[3] []()

[4] []()

[5] []()
