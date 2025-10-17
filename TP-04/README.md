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

**Palabras clave**:

---

## Introducción

---

## Resultados

### Consigna 1

Las redes pueden clasificarse según su alcance geográfico en diferentes categorías, dependiendo del tamaño del área que abarcan y del propósito para el cual se utilizan.

- **PAN (Personal Area Network)**: es la red de menor alcance que se utiliza para la interconexión de dispositivos personales en un espacio reducido, como una habitación o el entorno inmediato de una persona. Ejemplos comunes son las conexiones Bluetooth o infrarrojas entre un teléfono móvil, auriculares o una computadora portátil.
- **LAN (Local Area Network)**: abarca un área limitada, como una vivienda, oficina o edificio. Se caracteriza por ofrecer altas velocidades de transmisión y baja latencia. Es la más utilizada en entornos domésticos, empresariales y educativos para compartir recursos como impresoras o acceso a internet.
- **MAN (Metropolitan Area Network)**: cubre áreas más extensas, como una ciudad o un campus universitario. Su función principal es interconectar varias redes LAN dentro de una misma región, ofreciendo una comunicación rápida y estable. Suele ser utilizada por empresas o instituciones que requieren conexión entre distintas sedes dentro de una misma localidad.
- **WAN (Wide Area Network)**: es la red de mayor alcance, ya que puede conectar dispositivos o redes situadas en diferentes países o continentes. Utiliza infraestructuras de telecomunicaciones públicas y privadas, como satélites o cables submarinos. El mejor ejemplo de este tipo de red es Internet, que conecta millones de redes LAN y MAN a nivel mundial.

Una **VLAN (Virtual Local Area Network)** es una red local virtual que permite dividir una red física en varias redes lógicas independientes. Su objetivo principal es mejorar la seguridad, el rendimiento y la administración de la red, al separar el tráfico entre distintos grupos de usuarios o dispositivos, aunque todos estén conectados al mismo switch físico. Una VLAN permite que varios dispositivos compartan la misma infraestructura de red, pero funcionen como si estuvieran en redes distintas. Esto evita que el tráfico de un grupo interfiera con el de otro y facilita la organización según departamentos, funciones o niveles de acceso. Las VLAN se pueden *clasificar* según la forma en que se asignan los dispositivos:

- **VLAN estáticas (basadas en puertos)**: Son las más comunes. El administrador asigna manualmente cada puerto del switch a una VLAN específica. Los dispositivos conectados a ese puerto pertenecerán siempre a la misma VLAN.
- **VLAN dinámicas**: Asignan los dispositivos automáticamente a una VLAN según criterios como la dirección MAC, el protocolo o el usuario. Se configuran mediante un servidor de administración, lo que ofrece mayor flexibilidad.
- **VLAN por protocolo o subred**: Se agrupan los dispositivos que usan un mismo protocolo de red o pertenecen a una misma subred IP, sin depender del puerto físico al que estén conectados.

El protocolo **IEEE 802.1Q** es un estándar desarrollado por el Instituto de Ingenieros Eléctricos y Electrónicos (IEEE) que define el etiquetado o *“tagging”* de tramas Ethernet para identificar a qué VLAN pertenece cada paquete de datos dentro de una red. En una red con VLAN, varios grupos lógicos comparten el mismo enlace físico, por lo que es necesario un mecanismo que indique a qué VLAN pertenece cada trama que circula por el switch o el router. Aquí es donde actúa el estándar 802.1Q: agrega una etiqueta de 4 bytes dentro del encabezado Ethernet de cada trama, justo después de la dirección MAC de origen y destino. Esta etiqueta incluye el ID de VLAN (VID), que puede tener valores entre 1 y 4094, identificando de manera única a cada red virtual. El uso de IEEE 802.1Q permite que los switches y routers distingan el tráfico de múltiples VLAN en un mismo enlace físico, lo que se conoce como trunk o enlace troncal. Así, los dispositivos de red pueden mantener separados los flujos de datos de distintas VLAN, garantizando su aislamiento lógico.

En el contexto de las VLAN y del protocolo IEEE 802.1Q, el **tagging (etiquetado)** es el proceso mediante el cual se agrega una etiqueta especial a las tramas Ethernet para indicar a qué VLAN pertenece cada una. Cuando una trama se envía a través de un enlace troncal (trunk) —es decir, un enlace que transporta tráfico de múltiples VLAN—, el switch agrega esta etiqueta definida por el estándar 802.1Q. La etiqueta ocupa 4 bytes y contiene información clave, entre la cual se incluye el *Identificador de VLAN* (VLAN ID), que permite reconocer y separar el tráfico de cada red virtual. El *tagging* es fundamental para que los switches y routers puedan mantener el aislamiento lógico entre VLANs aun cuando los datos viajan por los mismos cables físicos. Cuando la trama llega a su destino, el switch receptor lee la etiqueta, identifica la VLAN correspondiente y luego la elimina (untagging) antes de entregarla al dispositivo final.

![Imagen Taggin](https://github.com/user-attachments/assets/a1417003-bfff-41a8-9b4f-455fcac35427)

---

## Discusión y conclusiones

---

## Referencias

[1] [TechTarget - IEEE 802 Wireless Standards Reference](https://www.techtarget.com/searchnetworking/reference/IEEE-802-Wireless-Standards-Fast-Reference)

[2] [Copperpod - A Comprehensive Comparison of Wi-Fi 5, 6, and 7](https://www.copperpodip.com/post/demystifying-wi-fi-a-comprehensive-comparison-of-wi-fi-5-6-and-7#:~:text=Conclusi%C3%B3n,y%20capaz%20hasta%20la%20fecha.)

[3] [Patch Box Blog - Fibra optica monomodo y multimodo](https://patchbox.com/es/blog/monomodo-multimodo-fibra-optica/)

[4] [Noticia sobre IFC](https://aws.amazon.com/es/blogs/networking-and-content-delivery/satellite-communication-on-aws-thales-cloudifies-in-flight-wifi-service/#:~:text=Descripci%C3%B3n%20general%20del%20Wi%2DFi%20a%20bordo%20de%20Thales&text=El%20sistema%20IFC%20de%20Thales,terrestres%20en%20cada%20ubicaci%C3%B3n%20geogr%C3%A1fica.)

[5] [Comparison of IoT Communication Protocols](https://research.aimultiple.com/iot-communication-protocol/)
