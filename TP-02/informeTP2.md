# Trabajo Practico N2

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

![Efecto-Doppler](img/efecto-doppler.png)

En la imagen se puede apreciar el efecto Doppler, el cual se ve representado en elcambio aparente en la frecuencia de la onda.
El efecto Doppler es el cambio aparente en la frecuencia (o longitud de onda) de una onda cuando existe movimiento relativo entre la fuente emisora y el observador, en este caso entre el barco y el satélite.

Características principales del efecto Doppler:

- La velocidad de propagación de la onda no cambia; lo que varía es la frecuencia y la longitud de onda observadas, la cual puede aumentar o disminuir segun se acerque o se aleje la fuente de ondas.

- Afecta a todo tipo de ondas: sonoras, electromagnéticas, etc.

- La magnitud del efecto depende de la velocidad relativa y de la dirección del movimiento (máximo cuando están en línea recta).

Como vimos en el trabajo anterior, el **espectro electromagnético** es la clasificación completa de toda la radiación electromagnética, organizada por su frecuencia o longitud de onda. Se divide en grandes regiones, que representan clasificaciones científicas para entender las propiedades físicas de las ondas. Las principales regiones son:

- **Ondas de radio:** Frecuencias más bajas (longitudes de onda más largas). Utilizadas en radiodifusión, comunicaciones inalámbricas y televisión.
- **Microondas:** Frecuencias más altas que las ondas de radio. Se usan en hornos de microondas, radares y Wi-Fi.
- **Infrarrojo:** Asociado con la radiación de calor. Se usa en termografía y mandos a distancia.
- **Luz visible:** La única región que el ojo humano puede percibir. Cada color corresponde a una frecuencia diferente.
- **Ultravioleta:** Frecuencias más altas que la luz visible. Responsable de las quemaduras solares.
- **Rayos X:** Usados en radiografías médicas.
- **Rayos gamma:** Las frecuencias más altas y con mayor energía. Producidas por fenómenos cósmicos y desintegración nuclear.

A diferencia de las regiones, las **bandas de transmisión** son divisiones más específicas y estrechas dentro de la **región de las ondas de radio y microondas**. Son asignadas y reguladas por organismos internacionales para usos de telecomunicaciones específicos y para evitar interferencias. Algunas bandas de transmicion son la banda FM para radio, las bandas 4G/5G para telefonía móvil, y las bandas de Wi-Fi.

El efecto Doppler, afecta a todas las ondas electromagnéticas. La magnitud del cambio de frecuencia es directamente proporcional a la frecuencia de la onda.

Las bandas de transmisión más afectadas son las que tienen frecuencias más altas las cuales experimentan el mayor desplazamiento de frecuencia absoluto. Esto es especialmente relevante en aplicaciones donde la velocidad es un factor importante, como en las comunicaciones con satélites en órbita baja o alta velocidad.

Las bandas de transmisión menos afectadas: son las bandas de transmisión con las frecuencias más bajas ya que experimentan un menor desplazamiento de frecuencia absoluto. Este efecto es menos crítico en bandas de radiodifusión de baja frecuencia como AM/FM, aunque sigue estando presente.

No, el efecto Doppler no esta relacionado la razón por la que se desaconseja usar celulares en aviones o sin tener activado el modo avión. Las razones son más bien de interferencia y regulación:\
Los dispositivos electrónicos personales como los celulares pueden emitir señales dentro de la misma banda de frecuencias que los sistemas de comunicación y navegación del avión, produciendo interferencias. Aunque los sistemas modernos están muy protegidos, sigue siendo una precaución.\
Las autoridades que regulan la aviación civil generalmente prohíben transmisiones celulares en vuelo por seguridad y coordinación de frecuencias, incluso si la interferencia real es mínima.

---

### Consigna 2

![Ruido-Electromagnetico](img/ruido-electromagnetico.png)

En la imagen se puede apreciar como el motor de corriente alterna de un taladro electrico provoca interferencia por ruido aditivo sobre una señal. Los motores electricos de corriente alterna generan corrientes pulsantes al conmutar o variar el flujo, estas corrientes producen campos electromagnéticos variables alrededor del motor y los cables.

Características principales de la interferencia por ruido aditivo:

- Amplio espectro: Suele afectar una amplia gama de frecuencias (ruido de banda ancha), aunque puede ser también selectivo en frecuencia dependiendo de la fuente.

- Energía limitada pero superpuesta: Aunque la energía de cada componente de ruido es pequeña, se suma a la señal deseada, dificultando su detección o decodificación.

- Origen eléctrico o electromagnético: Puede provenir de motores, equipos electrónicos, descargas atmosféricas, transmisión de radio cercana, etc.

- Impacto en la relación señal/ruido ($\text{SNR}$): Reduce la $\text{SNR}$, lo que aumenta la probabilidad de errores en sistemas digitales o distorsiona señales analógicas.

Influencia del la interferencia por ruido sobre:

- ASK: Modifica directamente la amplitud percibida por el receptor. Esto puede hacer que un “0” se interprete como un “1” y viceversa.\
  En qué medida: Muy sensible. Incluso ruido pequeño puede causar errores de bit, especialmente en canales con baja SNR.

- FSK: Tiene poca influencia sobre la frecuencia, por lo que los bits se detectan correctamente. FSK es muy resistente frente a ruido de amplitud, por eso se usa en canales ruidosos.

- QPSK: Desplaza los puntos de la constelación, aumentando la probabilidad de que el receptor decida el símbolo incorrecto.
  QPSK es moderadamente sensible, si bien es mucho mas resistente que ASK, puede fallar si la SNR baja demasiado.

- QAM: Mueve los símbolos en la constelación, especialmente en la dirección de amplitud, causando errores de símbolo.
  QAM presenta alta sensibilidad, especialmente en constelaciones densas (16-QAM, 64-QAM). QAM de baja orden (4-QAM, 8-QAM) tolera más ruido, al igual que sucede con el caso del efecto doppler.

El $\text{SNR}$ (Signal-Noise Ratio) Es la relación entre la potencia de la señal útil y la potencia del ruido en un canal de comunicación, se utiliza como medida de la calidad del canal, generalmente se mide en $\text{dB}$ (decibelios)

$$\text{SNR}_{\text{dB}} = 10\cdot\log_{10}{\left( \frac{P_{\text{señal}}}{P_{\text{ruido}}} \right)}$$

El $\text{SNR}$ tiene una relacion directa con el $\text{BER}$, ya que, a mayor de $\text{SNR}$ menor será el $\text{BER}$ y viceversa: a menor $\text{SNR}$ mayor será el $\text{BER}$.

## Referencias

[1] [How and why the Doppler Effect can impact the quality of wireless communications?](https://www.telecomhall.net/t/how-and-why-the-doppler-effect-can-impact-the-quality-of-wireless-communications/23159)

[2] [Wikipedia: Mobile phones on aircraft](https://en.wikipedia.org/wiki/Mobile_phones_on_aircraft)

[3] [Bit Error Rate Analysis of Digital Modulation Techniques
in Wireless Communication System](https://www.irejournals.com/formatedpaper/1703100.pdf)

[4] [Theoretical vs. simulated BER vs. SNR for ASK, FSK, and PSK](https://www.salimwireless.com/2023/08/ber-vs-snr-ask-fsk-psk.html)
