# Pasos para usar MQTT con el broker mosquitto en Linux Debian

## Instalacion de mosquitto

```bash
sudo apt update
sudo apt-get install mosquitto mosquitto-clients
```

## Verificar que funciona

```bash
service mosquitto status
```

## Programa

Recomendamos utilizar [Anaconda](https://www.youtube.com/watch?v=-8GWhLfekSs&t=365s) para gestionar los paquetes necesarios en entornos virtuales

Los paquetes que usamos son:

- `paho.mqtt`
- `random`
