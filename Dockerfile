# Utilizar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar las dependencias necesarias para pyheif
RUN apt-get update && apt-get install -y libheif-dev

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias de Python usando pip
RUN pip install --no-cache-dir Pillow pyheif

# Comando para ejecutar el script de conversión
CMD ["python", "convert_heic_to_png.py"]
