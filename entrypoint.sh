#!/bin/bash

# Crear migraciones
echo "Creando migrations"
python manage.py makemigrations

# Aplicar migraciones
echo "Aplicando migrations"
python manage.py migrate

# Iniciar servidor
echo "Iniciando servidor"
python manage.py runserver 0.0.0.0:8000