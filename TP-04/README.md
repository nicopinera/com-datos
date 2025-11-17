# Trabajo Practico N4

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

Este informe aborda el estudio teórico y práctico de las VLAN y su aplicación en el diseño de redes segmentadas. Se analizan los conceptos esenciales relacionados con la clasificación de redes, la organización lógica mediante VLANs, el estándar IEEE 802.1Q y el proceso de etiquetado de tramas. Posteriormente, se desarrolla la configuración de una red multi-VLAN en Packet Tracer, incluyendo la asignación de puertos, el uso de enlaces troncales, el enrutamiento inter-VLAN, DHCP, NAT y ACLs. Finalmente, se presenta un caso aplicado que simula la red interna de un avión, validando el comportamiento de cada segmento a través de pruebas de conectividad realistas.

**Palabras clave**:VLAN, IEEE 802.1Q, tagging, trunking, NAT, ACL, DHCP, segmentación, redes locales, enrutamiento inter-VLAN.

---

## Introducción

La segmentación lógica mediante VLAN se ha convertido en una herramienta fundamental para el diseño y administración de redes modernas. Estas permiten dividir una infraestructura física en múltiples dominios virtuales independientes, optimizando la seguridad, el rendimiento y el control del tráfico de datos. Comprender el funcionamiento de las VLAN y de estándares como IEEE 802.1Q resulta esencial para implementar soluciones escalables y organizadas en entornos empresariales, educativos e incluso escenarios específicos como el transporte aéreo.

Este informe se estructura en tres partes. En primer lugar, se revisan los conceptos teóricos sobre la clasificación de redes según su alcance, los tipos de VLAN disponibles y el mecanismo de etiquetado utilizado para transportar tráfico multi-VLAN. En segundo lugar, se desarrolla una experiencia práctica en Packet Tracer donde se configuran VLAN estáticas, asignación de puertos y enlaces troncales entre switches. Finalmente, se presenta un caso integrado que simula la red de un avión, aplicando técnicas de enrutamiento inter-VLAN, DHCP, ACLs y NAT para establecer diferentes niveles de acceso según el segmento de usuarios. Este enfoque teórico-práctico permite comprender el funcionamiento integral de una red segmentada y su relevancia en escenarios reales.

---

## Resultados

### Consigna 1

Las redes pueden clasificarse según su alcance geográfico en diferentes categorías, dependiendo del tamaño del área que abarcan y del propósito para el cual se utilizan.

- **PAN (Personal Area Network)**: es la red de menor alcance que se utiliza para la interconexión de dispositivos personales en un espacio reducido, como una habitación o el entorno inmediato de una persona. Ejemplos comunes son las conexiones Bluetooth o infrarrojas entre un teléfono móvil, auriculares o una computadora portátil.
- **LAN (Local Area Network)**: abarca un área limitada, como una vivienda, oficina o edificio. Se caracteriza por ofrecer altas velocidades de transmisión y baja latencia. Es la más utilizada en entornos domésticos, empresariales y educativos para compartir recursos como impresoras o acceso a internet.
- **MAN (Metropolitan Area Network)**: cubre áreas más extensas, como una ciudad o un campus universitario. Su función principal es interconectar varias redes LAN dentro de una misma región, ofreciendo una comunicación rápida y estable. Suele ser utilizada por empresas o instituciones que requieren conexión entre distintas sedes dentro de una misma localidad.
- **WAN (Wide Area Network)**: es la red de mayor alcance, ya que puede conectar dispositivos o redes situadas en diferentes países o continentes. Utiliza infraestructuras de telecomunicaciones públicas y privadas, como satélites o cables submarinos. El mejor ejemplo de este tipo de red es Internet, que conecta millones de redes LAN y MAN a nivel mundial.

Una **VLAN (Virtual Local Area Network)** es una red local virtual que permite dividir una red física en varias redes lógicas independientes. Su objetivo principal es mejorar la seguridad, el rendimiento y la administración de la red, al separar el tráfico entre distintos grupos de usuarios o dispositivos, aunque todos estén conectados al mismo switch físico. Una VLAN permite que varios dispositivos compartan la misma infraestructura de red, pero funcionen como si estuvieran en redes distintas. Esto evita que el tráfico de un grupo interfiera con el de otro y facilita la organización según departamentos, funciones o niveles de acceso. Las VLAN se pueden _clasificar_ según la forma en que se asignan los dispositivos:

- **VLAN estáticas (basadas en puertos)**: Son las más comunes. El administrador asigna manualmente cada puerto del switch a una VLAN específica. Los dispositivos conectados a ese puerto pertenecerán siempre a la misma VLAN.
- **VLAN dinámicas**: Asignan los dispositivos automáticamente a una VLAN según criterios como la dirección MAC, el protocolo o el usuario. Se configuran mediante un servidor de administración, lo que ofrece mayor flexibilidad.
- **VLAN por protocolo o subred**: Se agrupan los dispositivos que usan un mismo protocolo de red o pertenecen a una misma subred IP, sin depender del puerto físico al que estén conectados.

El protocolo **IEEE 802.1Q** es un estándar desarrollado por el Instituto de Ingenieros Eléctricos y Electrónicos (IEEE) que define el etiquetado o _“tagging”_ de tramas Ethernet para identificar a qué VLAN pertenece cada paquete de datos dentro de una red. En una red con VLAN, varios grupos lógicos comparten el mismo enlace físico, por lo que es necesario un mecanismo que indique a qué VLAN pertenece cada trama que circula por el switch o el router. Aquí es donde actúa el estándar 802.1Q: agrega una etiqueta de 4 bytes dentro del encabezado Ethernet de cada trama, justo después de la dirección MAC de origen y destino. Esta etiqueta incluye el ID de VLAN (VID), que puede tener valores entre 1 y 4094, identificando de manera única a cada red virtual. El uso de IEEE 802.1Q permite que los switches y routers distingan el tráfico de múltiples VLAN en un mismo enlace físico, lo que se conoce como trunk o enlace troncal. Así, los dispositivos de red pueden mantener separados los flujos de datos de distintas VLAN, garantizando su aislamiento lógico.

En el contexto de las VLAN y del protocolo IEEE 802.1Q, el **tagging (etiquetado)** es el proceso mediante el cual se agrega una etiqueta especial a las tramas Ethernet para indicar a qué VLAN pertenece cada una. Cuando una trama se envía a través de un enlace troncal (trunk) —es decir, un enlace que transporta tráfico de múltiples VLAN—, el switch agrega esta etiqueta definida por el estándar 802.1Q. La etiqueta ocupa 4 bytes y contiene información clave, entre la cual se incluye el _Identificador de VLAN_ (VLAN ID), que permite reconocer y separar el tráfico de cada red virtual. El _tagging_ es fundamental para que los switches y routers puedan mantener el aislamiento lógico entre VLANs aun cuando los datos viajan por los mismos cables físicos. Cuando la trama llega a su destino, el switch receptor lee la etiqueta, identifica la VLAN correspondiente y luego la elimina (untagging) antes de entregarla al dispositivo final.

![Imagen Taggin](https://github.com/user-attachments/assets/a1417003-bfff-41a8-9b4f-455fcac35427)

### Consigna 2

![Red Parte 1](https://github.com/user-attachments/assets/a2e8f9fb-3ad8-459b-926f-d8db64e57c2d)

La Vlan que se usa por defecto es la vlan 1:

![Vlan brief](https://github.com/user-attachments/assets/724b5f9d-b6ef-4929-8a50-4a521d22afa5)

Luego de crear las vlans, asignar la vlan 99 a la ip de management y la PC-A a Laboratorio:

![Vlan e IP](https://github.com/user-attachments/assets/133f8772-0264-42e3-9335-d9c39d3c412c)

Como se puede observar la Vlan99 aparece con el estado `protocol: down` porque no hay trafico ni puertos activos en esa Vlan

![Ping entre compus](https://github.com/user-attachments/assets/f5f57340-8bb1-4dae-a184-664c319c474e)

![Ping entre switches](https://github.com/user-attachments/assets/836c3cfe-0076-46ed-9506-ec4095a193d7)

### Consigna 3

Diagrama de red:

![Diagrama de Red](https://github.com/user-attachments/assets/74af502c-417b-4efb-9828-850c196fc7e9)

Realizamos las configuraciones necesarias en el switch, el router del avión e ISP y el servidor:

![Switch](https://github.com/user-attachments/assets/c1c68609-1ff3-4a66-95a1-ff2c1963aafb)

![Router](https://github.com/user-attachments/assets/cf7b44ed-9e0d-43a5-a2d5-281a35adfe69)

Y ahora podemos realizar las siguientes pruebas:

![pruebas a realizar](https://github.com/user-attachments/assets/0fc69984-6fbc-46eb-8005-b30f2e66c5cc)

En el PC-Turista:

![Turista1](https://github.com/user-attachments/assets/f27c17de-91a7-484f-b954-9362e1f21f26)

![Turista2](https://github.com/user-attachments/assets/ae0c6f6b-6675-4f2e-a85e-f871d5042fc7)

![Turista3](https://github.com/user-attachments/assets/ad870906-eebe-4824-92f8-6f7f4c2f138f)

En el PC-Business:

![Buissness1y3](https://github.com/user-attachments/assets/490e6d7a-8d93-411b-8d1b-41b2da3d3219)

![Buissness2](https://github.com/user-attachments/assets/64ab7831-8e0e-4bf5-8cc2-dca7dffb6b43)

Y finalmente probamos conectividad con PC-Admin:

![Admin1](https://github.com/user-attachments/assets/89fe7eec-95d2-4a1e-b96f-bff5de4c1eff)

![Admin2](https://github.com/user-attachments/assets/626ec1ca-4f32-4222-88c7-7cf9ff48f42d)

![Admin3](https://github.com/user-attachments/assets/810409cb-65d7-427f-912c-0948e0b9041a)

![Admin4](https://github.com/user-attachments/assets/b6f4a9c4-133f-40f8-a54e-a10fe940ea3b)

La red del avión que hemos diseñado usa VLANs para separar y aislar los distintos tipos de pasajeros y servicios. La VLAN 10 (Turista), la VLAN 20 (Business) y la VLAN 99 (Administración) nos permiten segmentar el tráfico, evitando que equipos de diferentes categorías se comuniquen directamente y mejorando la seguridad y el control dentro del entorno.

Para el acceso a Internet, se configuró NAT únicamente sobre la VLAN Business. De esta forma, solo los dispositivos de esta clase pueden traducir sus direcciones privadas y salir hacia la red externa a través del router. Esto garantiza que los pasajeros de Turista no tengan salida a Internet y que cada segmento tenga una política de acceso diferenciada.

Finalmente, se aplicó una ACL (Access Control List) sobre la VLAN Turista que bloquea todo el tráfico destinado a Internet, permitiendo únicamente el acceso al servidor local de entretenimiento ubicado en la VLAN de Administración. Esto asegura que Turista solo tenga acceso al contenido interno, mientras que Business y Administración mantienen sus privilegios de conectividad según lo planificado.

---

## Discusión y conclusiones

Gracias a este trabajo práctico pudimos analizar los fundamentos teóricos de las VLAN, el estándar IEEE 802.1Q y el proceso de etiquetado de tramas, conceptos esenciales para entender cómo múltiples redes lógicas pueden coexistir en una única infraestructura física. La implementación práctica reforzó estos conocimientos, mostrando cómo la asignación de puertos, la configuración de enlaces troncales y el enrutamiento inter-VLAN permiten controlar el flujo de tráfico entre distintos grupos de usuarios.

Además, vimos como se aplican tecnologías complementarias que resultan fundamentales en redes reales: DHCP para automatizar la asignación de direcciones, ACLs para definir políticas de acceso precisas y NAT para gestionar la salida a Internet de segmentos específicos. Las pruebas realizadas validaron el comportamiento esperado de cada parte de la topología, demostrando que la combinación de estos mecanismos permite construir redes flexibles y seguras, adaptadas a diferentes necesidades operativas. En definitiva, este trabajo facilitó la integración de teoría y práctica, proporcionando una visión completa del diseño y administración de redes segmentadas.

---
