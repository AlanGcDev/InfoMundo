#!/bin/bash
# Crear la carpeta de staticfiles si no existe
mkdir -p staticfiles
# Colectar los archivos estáticos
python3 manage.py collectstatic --noinput
