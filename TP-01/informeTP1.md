# Trabajo Practico N1 - Repaso de fundamentos esenciales e introduccion a Packet Tracer

## Nombres

- Nicolas Piñera
- Julian Krede
- Noelia

**Nombre del grupo**: Puerto1337

## UNC - Facultad de Ciencias Exactas, Físicas y Naturales

## Cátedra: Comunicaciones de Datos

### Profesores

**Fecha** 11/8/2025

---

## Información de los autores

- **Información de contacto**:
  - [nicolas.pinera@mi.unc.edu.ar](mailto:nicolas.pinera@mi.unc.edu.ar)
  - [julian.krede@mi.unc.edu.ar](mailto:julian.krede@mi.unc.edu.ar)

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

En comunicaciones de datos, los dispositivos que operan en la banda de microondas incluyen principalmente enlaces de microondas punto a punto, sistemas de radio por microondas con frecuencia modulada y unidades móviles de microondas. Estos dispositivos utilizan antenas, transmisores, receptores y otros componentes para transmitir datos a través de ondas electromagnéticas en frecuencias de microondas. Por ejemplo:

- Enlaces de microondas punto a punto
- Sistemas de radio por microondas con frecuencia modulada
- Unidades móviles de microondas

La línea roja que se puede ver en nuestra figura representa la atenuación de la onda electromagnética, la cual es la pérdida de intensidad de la señal a medida que se propaga a través del espacio. Este fenómeno se debe a varios factores, como la dispersión, la absorción y la reflexión. En la imagen, se ve cómo la amplitud de la onda, va disminuyendo a medida que la onda viaja por el espacio. Es importante destacar que la atenuación no solo afecta la potencia de la señal, sino que también puede distorsionarla y degradar su calidad, lo que se traduce en problemas de conexión, pérdida de datos y un rendimiento general más lento.

- Reducción de la Intensidad de la Señal
- Aumento de la Tasa de Error de Bits (BER)
- Disminución de la Velocidad de Datos
- Inestabilidad de la Conexión y Desconexione
- Calidad Degradada de Audio y Video

Claramente sí podemos observar los efectos de la atenuación en la vida cotidiana como señal de Wi-Fi, cuando te alejas de nuestro router, la intensidad de la señal de Wi-Fi en nuestro teléfono o computadora disminuye. Esto se manifiesta en una velocidad de conexión más lenta, o incluso en la pérdida total de la conexión. Este fenomeno tambien afecta a los diferentes tipos de redes y transmiciones como la de cable coaxial, telefono celular y fibra optica [2]

---

### Consigna 2

A continuacion, se realizara un analisis del siguiente sistema de comunicacion.

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

### Consigna 4

Utilizando el software de Packet Tracer se realizo la simulacion pedida en el enunciado. Una vez configurado el Router Wireless tanto su IP, nombre de red y contraseña, podemos ver que el mismo trabaja en el canal de frecuencia $2.4[GHz]$ el cual pertenece a la region de **microondas**. Dentro de esta región, opera en la banda **ISM** (Industrial, Scientific and Medical), que va de 2.400 GHz a 2.4835 GHz. Esta es una banda de frecuencia de uso libre y no requiere licencia para la mayoría de las aplicaciones. [7]

---

## Conclusiones

## Referencias

[1] [Espectro electromagentico](https://concepto.de/espectro-electromagnetico/)  
[2] [Atenuacion en Redes](https://opticanaranjo.com.ar/atenuaciones-en-redes-industriales-opticas/)  
[3] [Comunicacion Sincronica y Asincronica](https://isaaclp.wordpress.com/redes-i-programa-de-la-materia/unidad-i/interfaces-de-comunicaciones/transmision-sincrona-y-asincrona/)  
[4] [Modos de comunicacion](https://www.scaler.com/topics/computer-network/transmission-modes-computer-networks/)  
[5] [Codigo ASCII](https://elcodigoascii.com.ar/codigos-ascii/letra-r-minuscula-codigo-ascii-114.html)  
[6] [Modulaciones](https://abcxperts.com/las-modulaciones-digitales-como-funcionan-y-por-que-son-importantes/?srsltid=AfmBOop7KtQXNy-PC3_qXwbZskX8POyfhIWRIeygYYEaBo7HBzDKwIab)  
[7] [Banda ISM](https://www.data-alliance.net/es/banda-de-frecuencias-ism-y-su-distribuci%C3%B3n)
