# Variables
PROGRAMA1 = comDatos/TPs/TP5
PROGRAMA2 = lan/deviceA/status

# Instalar mosquitto
install_mosquitto:
	sudo apt update;\
	sudo apt-get install mosquitto mosquitto-clients

# Comprobar funcionamiento, depende de estar instalado
start_mosquitto:
	sudo service mosquitto start;\
	sudo service mosquitto status

python:
	cd TP-05;\
	python3 -m venv venv;\
	. venv/bin/activate;\
	python -m pip install --upgrade pip;\
	python -m pip install -r requerimientos.txt

terminal_holaMundo:
	mosquitto_sub -h localhost -t '$(PROGRAMA1)' -v

terminal:
	mosquitto_sub -t "#" -v

terminal_pub:
	mosquitto_sub -h localhost -t '$(PROGRAMA2)' -v

.PHONY: install_mosquitto verificar install_dep activate start_mosquitto
