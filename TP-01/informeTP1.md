# Trabajo Practico N1 - Repaso de fundamentos esenciales e introduccion a Packet Tracer

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

**Fecha:** 18/8/2025

---

## Información de los autores

- **Información de contacto**:

  - [nicolas.pinera@mi.unc.edu.ar](mailto:nicolas.pinera@mi.unc.edu.ar)
  - [julian.krede@mi.unc.edu.ar](mailto:julian.krede@mi.unc.edu.ar)
  - [noelia.valarezo@mi.unc.edu.ar](mailto:noelia.valarezo@mi.unc.edu.ar)
  - email noe

---

## Resumen

**Palabras clave**:

---

## Introducción

---

## Resultados

### Consigna 1

A partir del siguiente grafico de una onda electromagentica se realizara un repaso de ellas, modulacion/demodulacion, señales de tiempos continuo, señales de tiempo discreto.

![Imagen1](/TP-01/img/image.png)

A partir de lo visto en la materia Fisica 3 sabemos que:

$$c = \lambda * f$$

Siendo:

- $c$: Velocidad de la luz en el vacío (aproximadamente $3*10^8 [\frac{m}{s}]$)
- $\lambda$: Longitud de onda (en metros)
- $f$: Frecuencia (en hertz)

Para este grafico podemos saber que $\lambda = 120 - 60 = 60 [mm] = 60*10^{-3} [m]$.

Por ende, podemos calcular la frecuencia $f$:

$$f = \frac{c}{\lambda} = \frac{3 * 10^8}{60 * 10^{-3}} = 5000000000 [Hz] = 5*10^9 [Hz] = 5[GHz]$$

El espectro electromagnético es la distribución de energías de las radiaciones electromagnéticas. Se puede expresar en términos de la longitud de onda y frecuencias de las radiaciones. Se extiende desde las radiaciones con menor longitud de onda (los rayos gamma) hasta las de mayor longitud de onda (las ondas de radio). [1]

Se compone de diversos subrangos o porciones, cuyos límites no son del todo definidos y tienden a superponerse. Cada franja del espectro se distingue de las otras en el comportamiento de sus ondas durante la emisión, transmisión y absorción, así como en sus aplicaciones prácticas.

Las características de dicha distribución dependen de la frecuencia o la longitud de onda de las oscilaciones, así como de su energía. Las tres cantidades están asociadas entre sí: a un dada una longitud de onda le corresponde una frecuencia y una energía determinadas.

El espectro electromagnético hasta el momento se ha podido conocer algunas de sus regiones, conocidas como bandas o segmentos. Estas son:

![Espectro Electromagnetico](/TP-01/img/emspecsmall.jpg)

Para nuestra onda electromagnetica descripta en la grafica, su longitud de onda es de $\lambda=60*10^{-3}[m]$ y frecuencia $f=5[GHz]$ pertenece a la banda de las **Microondas** las cuales se utilizan en hornos microondas, redes Wi-Fi, radares y sistemas de comunicación por satélite. (capaz se puede desarrollar un poco mas)

En esa franja trabajan muchos dispositivos, tanto de uso cotidiano como industriales o militares, algunos de estos son:

- Hornos microondas (~2,45 GHz).
- Dispositivos que cuentan con los siguientes tipos de comunicación inalámbrica:
  - Wi-Fi (2,4 GHz y 5 GHz, algunas variantes hasta 6 GHz).
  - Bluetooth (2,4 GHz)
  - Telefonía móvil (algunas bandas de 1–6 GHz y también 24–40 GHz en 5G).
  - Enlaces de microondas terrestres punto a punto.
- Radares como por ejemplo: radares meteorológicos, de aviación y militares.
- Radiotelescopios.

La línea roja que se puede ver en nuestra figura representa la atenuación de la onda electromagnética, la cual es la pérdida de intensidad de la señal a medida que se propaga a través del espacio. Este fenómeno se debe a varios factores, como la dispersión, la absorción y la reflexión. En la imagen, se ve cómo la amplitud de la onda, va disminuyendo a medida que la onda viaja por el espacio. Es importante destacar que la atenuación no solo afecta la potencia de la señal, sino que también puede distorsionarla y degradar su calidad, lo que se traduce en problemas de conexión, pérdida de datos y un rendimiento general más lento.

- Reducción de la Intensidad de la Señal
- Aumento de la Tasa de Error de Bits (BER)
- Disminución de la Velocidad de Datos
- Inestabilidad de la Conexión y Desconexione
- Calidad Degradada de Audio y Video

Claramente sí podemos observar los efectos de la atenuación en la vida cotidiana como señal de Wi-Fi, cuando te alejas de nuestro router, la intensidad de la señal de Wi-Fi en nuestro teléfono o computadora disminuye. Esto se manifiesta en una velocidad de conexión más lenta, o incluso en la pérdida total de la conexión. Este fenomeno tambien afecta a los diferentes tipos de redes y transmiciones como la de cable coaxial, telefono celular y fibra optica [2]

---

### Consigna 2

A continuación, se realizara un análisis del siguiente sistema de comunicación.

![Sistema](/TP-01/img/image2.png)

Como se observa, nuestro sistema esta formado por un transmisor y un receptos. Nuestro transmisor es el encargado de enviar la informacion y ademas una señal de clock para podes sincronizar la comunicacion. Dado que la comunicacion se da en un solo sentido entonces se esta realizando una transmision de tipo **sincronica** y de modo **simple** o **unidireccional** [3] [4]. Si nosotros queremos transmitir de manera rapida y bidireccional, tendriamos que cambiar el modo de transmision, a un modo **Full duplex** permitiendo que los datos viajen en ambas direcciones al mismo tiempo, ademas al ser **sincronica** permite una alta eficiencia y velocidad para enviar datos de manera continua.

Si nosotros quisieramos envial la letra "r" por medio de una señal digital en una comunicacion UART deberiamos buscar su representacion en ASCII que es el numero $114$ y convertirlo a binario, lo que resulta la siguiente cadena $01110010$ y lo que se tranmsitiria seria :

![r-binario](/TP-01/img/r-binario.png)

Y el mejor momento para muestrear la señal seria a la mitad del periodo de nuestra señal de clock, ya que en ese instante la tension que representaria nuestro 1 o 0 logico ya se encuentra establecida.
[5]

---

### Consiga 3

Transmitir una señal escalonada de forma inalámbrica no es ideal debido a la sensibilidad de este tipo de señal a las interferencias y la atenuación que sufre al atravesar obstáculos, lo que puede degradar la calidad de la señal y dificultar la recepción precisa.

Las señales escalonadas, también llamadas señales de pulso, son susceptibles a la interferencia de otras señales electromagnéticas presentes en el entorno inalámbrico. Los obstáculos físicos como paredes, muebles e incluso el cuerpo humano pueden absorber o reflejar parte de la señal, debilitándola considerablemente. En el caso de las señales escalonadas, la atenuación puede hacer que la señal se vuelva demasiado débil para ser detectada correctamente. Las señales escalonadas pueden requerir un ancho de banda considerable para su transmisión, lo que puede entrar en conflicto con otras señales en el mismo espectro, especialmente en redes inalámbricas congestionadas.

En resumen, aunque una señal escalonada es una forma de representar datos digitales, no es apta para la transmisión inalámbrica debido a la necesidad de un ancho de banda infinito y a la distorsión que sufre la señal al ser filtrada por el canal de transmisión.

En la siguiente grafica lo que se puede ver es una modulacion **PSK** la cual es una técnica de modulación digital que varía la fase de una onda portadora para representar información digital. La señal digital a modular se utiliza para cambiar la fase de la señal portadora, creando diferentes patrones de fase que representan los datos.

![PSK](/TP-01/img/modulacion.png)

A continuacion se vera el resultado de realizar una modulacion PSK para el siguiente dato a transmitir: **01110110**

![PSK Ejercicio](/TP-01/img/modulacionPSKEjercicio.png)

Ademas de esta modulacion digital, existen otras maneras las cuales son:

- Modulación de Frecuencia (FSK – Frequency Shift Keying): se modula la frecuencia de la onda portadora para representar los bits. Puede haber dos o más frecuencias para representar diferentes valores binarios.
- Modulación de Amplitud (ASK – Amplitude Shift Keying): se modula la amplitud de la onda portadora para representar los bits. La presencia o ausencia de la señal en un intervalo de tiempo determinado indica un valor binario.
- Modulación por Desplazamiento de Fase Cuadratura (QPSK – Quadrature Phase Shift Keying): Es una variante de PSK en la que se transmiten dos bits por símbolo mediante cambios en la fase de la onda portadora.
- Modulación de Amplitud en Cuadratura (QAM): se modulan simultáneamente la amplitud y la fase de la onda portadora. Esto permite representar múltiples bits por símbolo, ya que cada símbolo puede tener diferentes combinaciones de amplitud y fase. [6]

![Modulaciones Digitales](/TP-01/img/Modulacion-digital.png)

---

### Consiga 4

Al realizar el experimento se observa que el router opera entre las frecuencia de $2,412\, \text{[GHz]}$ y $2,462 \, \text{[GHz]}$ conocida comunmente con la banda de $2,4\, \text{[GHz]}$, esta banda pertenece al espectro de microondas anteriormente mencionado.

#### Diagrama topologico de la red

![diagrama topologico](/TP-01/img/diagrama-topologico-pt.png)

#### Verificación de conectividad entre dispositivos

![ping-pc-a-notebook](/TP-01/img/ping-pc-a-notebook.png)

Como se puede observar se enviaron 4 paquetes desde _PC_ a _Notebook_ y este respondió a todos mostrando que hay una conexión establecida entre _PC_ y _Notebook_

#### Notebook dentro del alcance del router

![ping-notebookExt-a-notebook](/TP-01/img/ping-notebookExt-a-notebook.png)

Como se puede observar se tiene otro dispositivo _NotebookExt_ conectador a la red y dentro del alcance del router, al realizar la prueba de conectividad se observa que hay una conexión establecida entre este y _PC_

#### Notebook fuera del alcance del router

![ping-notebookExt-a-notebook](/TP-01/img/ping-notebookExt-a-notebook-fuera-de-rango.png)

Al mover el dispositivo _NotebookExt_ fuera del rango de alcance de router se observa como este pierde la conexión.

Ademas al realizar los experimentos se observó como a medida que el dispositivo _NotebookExt_ se aleja el tiempo medio de envío y recepción de paquetes es cada vez mayor.

---

## Conclusiones

En este trabajo práctico se realizó un repaso de conceptos fundamentales relacionados con las ondas electromagnéticas, los sistemas de comunicación y las modulaciones digitales. A través de los ejercicios y experimentos realizados, se pudo observar cómo las propiedades de las ondas, como la frecuencia y la longitud de onda, determinan su comportamiento y aplicaciones prácticas.

Además, se analizaron diferentes modos de transmisión y técnicas de modulación, destacando sus ventajas y limitaciones en distintos escenarios. Los experimentos con redes inalámbricas permitieron comprender cómo factores como la atenuación y el alcance afectan la conectividad y el rendimiento de los dispositivos.

En resumen, este trabajo permitió consolidar conocimientos teóricos y prácticos esenciales para el estudio de las comunicaciones de datos, sentando una base sólida para abordar temas más avanzados en la materia.

## Referencias

[1] [Espectro electromagentico](https://concepto.de/espectro-electromagnetico/)  
[2] [Atenuacion en Redes](https://opticanaranjo.com.ar/atenuaciones-en-redes-industriales-opticas/)  
[3] [Comunicacion Sincronica y Asincronica](https://isaaclp.wordpress.com/redes-i-programa-de-la-materia/unidad-i/interfaces-de-comunicaciones/transmision-sincrona-y-asincrona/)  
[4] [Modos de comunicacion](https://www.scaler.com/topics/computer-network/transmission-modes-computer-networks/)  
[5] [Codigo ASCII](https://elcodigoascii.com.ar/codigos-ascii/letra-r-minuscula-codigo-ascii-114.html)  
[6] [Modulaciones](https://abcxperts.com/las-modulaciones-digitales-como-funcionan-y-por-que-son-importantes/?srsltid=AfmBOop7KtQXNy-PC3_qXwbZskX8POyfhIWRIeygYYEaBo7HBzDKwIab)  
[7] [Banda ISM](https://www.data-alliance.net/es/banda-de-frecuencias-ism-y-su-distribuci%C3%B3n)
