# Variables
VENV = venv
ACTIVATE = . $(VENV)/bin/activate

# Instalar mosquitto
install_mosquitto:
	sudo apt update;\
	sudo apt-get install mosquitto mosquitto-clients

# Comprobar funcionamiento, depende de estar instalado
verificar:
	sudo service mosquitto status

venv:
ifeq ($(OS),Windows_NT) 
	python -m venv $(VENV) 
else
	python3 -m venv $(VENV) 
endif

# Creacion del entorno virtual e instalacion dependencias
install_dep: venv
	$(ACTIVATE) && pip install -r requerimientos.txt

# Iniciar mosquitto
start_mosquitto:
	sudo service mosquitto start

.PHONY: install_mosquitto verificar install_dep activate start_mosquitto
