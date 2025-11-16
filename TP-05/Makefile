# Variables
VENV = venv
ACTIVATE = . $(VENV)/bin/activate
ACTIVATE_W = $(VENV)\Scripts\activate
PROGRAMA1 = ./programas/pub_hello_world.py
PROGRAMA2 = ./programas/publisher_4a.py
PROGRAMA3 = ./programas/suscriber_4a.py

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
ifeq ($(OS),Windows_NT) 
	$(ACTIVATE_W) &&  python.exe -m pip install --upgrade pip && pip install -r requerimientos.txt
else
	$(ACTIVATE) && pip install -r requerimientos.txt
endif

act_venv:
ifeq ($(OS),Windows_NT) 
	$(ACTIVATE_W) && python.exe $(PROGRAMA1) && python.exe $(PROGRAMA2) && python.exe $(PROGRAMA3)
else
	$(ACTIVATE) && python.exe $(PROGRAMA1) && python.exe $(PROGRAMA2) && python.exe $(PROGRAMA3)
endif

# Iniciar mosquitto
start_mosquitto:
	sudo service mosquitto start

.PHONY: install_mosquitto verificar install_dep activate start_mosquitto
