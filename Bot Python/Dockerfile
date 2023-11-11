# Usar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requisitos y los archivos .py
COPY requirements.txt /app/
COPY *.py /app/

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Informar a Docker que el contenedor escucha en el puerto 5000 en tiempo de ejecución
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]