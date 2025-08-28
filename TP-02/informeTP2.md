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

En la imagen se puede apreciar el efecto Doppler, el cual afecta a la comunicación inalámbrica entre el barco y el satélite.
El efecto Doppler es el cambio aparente en la frecuencia (o longitud de onda) de una onda cuando existe movimiento relativo entre la fuente emisora y el observador, en este caso entre el barco y el satélite.

Características principales del efecto Doppler:

- La velocidad de propagación de la onda no cambia; lo que varía es la frecuencia y la longitud de onda observadas.

- Afecta a todo tipo de ondas: sonoras, electromagnéticas, etc.

- La magnitud del efecto depende de la velocidad relativa y de la dirección del movimiento (máximo cuando están en línea recta).

Recordando que anteriormente mencionamos los tipos de modulación como FSK, QPSK, ASK y QAM.\

Influencia del efecto doppler sobre:

- ASK: Produce un desplazamiento de frecuencia. Aunque la amplitud nominal no cambia, el receptor suele tener filtros pasabanda centrados en la frecuencia esperada. Si la portadora se desplaza, la señal se atenúa al pasar por el filtro, lo que puede confundir la detección de los niveles de amplitud.\
ASK es muy sensible a Doppler, especialmente en enlaces estrechos y cuerpos con alta velocidad relativa. Incluso unos pocos $kHz$ de desplazamiento pueden causar errores significativos.

- FSK: Al desplazar todas las frecuencias, cambia la diferencia entre “0” y “1”. Si el desplazamiento es comparable a la separación de las frecuencias, el receptor puede confundir un bit con otro.\
FSK es menos sensible al efecto doppler dado que solo basta con ajustar la separación de las frecuencias que representa los “0” y “1” para mitigar el efecto.

- QPSK: Causa un desplazamiento de frecuencia, que se traduce en rotación de fase progresiva de la señal recibida. Esto puede mover la constelación de símbolos y causar errores de decodificación si la sincronización de fase no se ajusta.\
QPSK es menos sensible que ASK o FSK; los sistemas modernos incluyen PLL o sincronización adaptativa, permitiendo tolerar velocidades moderadas sin degradación significativa.

- QAM: Afecta tanto fase como frecuencia efectiva, generando desplazamiento en la constelación compleja. Esto puede causar errores de símbolo porque tanto la amplitud como la fase se interpretan mal.\
QAM presenta mucha sensibilidad en constelaciones densas (16-QAM, 64-QAM), esto sucede porque los símbolos están cerca entre sí. Por lo tanto a mayor densidad, menor tolerancia a Doppler.

No, el efecto Doppler no tiene nada que ver con la razón por la que se desaconseja usar celulares en aviones o sin tener activado el modo avión. Las razones son más bien de interferencia y regulación:\
Los dispositivos electrónicos personales como los celulares pueden emitir señales dentro de la misma banda de frecuencias que los sistemas de comunicación y navegación del avión, produciendo interferencias. Aunque los sistemas modernos están muy protegidos, sigue siendo una precaución.\
Las autoridades que regulan la aviación civil generalmente prohíben transmisiones celulares en vuelo por seguridad y coordinación de frecuencias, incluso si la interferencia real es mínima.

## Referencias

[1] [How and why the Doppler Effect can impact the quality of wireless communications?](https://www.telecomhall.net/t/how-and-why-the-doppler-effect-can-impact-the-quality-of-wireless-communications/23159)

[2] [Wikipedia: Mobile phones on aircraft](https://en.wikipedia.org/wiki/Mobile_phones_on_aircraft)
