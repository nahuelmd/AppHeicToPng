# Convertidor de Imágenes HEIC a PNG

Este proyecto simplifica la conversión de imágenes en formato HEIC a PNG utilizando Docker. Es ideal para usuarios que desean convertir imágenes de dispositivos Apple a un formato más compatible como PNG.

## Pre-requisitos

- Docker instalado en tu máquina.

## Configuración Inicial

Primero, asegúrate de tener Docker instalado y funcionando en tu sistema. Luego, sigue estos pasos para preparar y utilizar la herramienta de conversión.

### Paso 1: Clonar el Repositorio

Abre una terminal y clona este repositorio usando el siguiente comando:

```bash
git clone [URL_DEL_REPOSITORIO]
cd AppHeicToPng
```

### Paso 2: Construir la Imagen Docker

Construye la imagen Docker del proyecto ejecutando:

```bash
docker build -t appheictopng .
```

Este paso solo es necesario la primera vez o cuando se actualice el proyecto.

### Uso

Para convertir imágenes de HEIC a PNG, sigue estos pasos:

1. Coloca tus archivos `.HEIC` en el directorio `source`.
2. Asegúrate de que el directorio `output` esté vacío o listo para recibir las nuevas imágenes.
3. Ejecuta el contenedor Docker con el siguiente comando:

```bash
docker run --rm -v "$(pwd)/source:/app/source" -v "$(pwd)/output:/app/output" appheictopng
```

Este comando monta los directorios `source` y `output` del directorio actual del proyecto dentro del contenedor y ejecuta el proceso de conversión.

Las imágenes convertidas se guardarán en el directorio `output`.

## Notas

- Este proyecto asume que estás trabajando en un entorno Unix-like, como Linux o macOS.
- Para usuarios de Windows, el comando para ejecutar el contenedor puede requerir ajustes, especialmente en la manera de especificar las rutas de los volúmenes.

## Contribuciones

Si tienes sugerencias o mejoras, por favor, siente libre de contribuir al proyecto. Abre un issue o un pull request con tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Esto significa que tienes amplia libertad para modificar, distribuir y usar el proyecto como desees, siempre y cuando incluyas el aviso de licencia original y las condiciones de copyright.
