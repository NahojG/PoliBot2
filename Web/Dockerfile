
# Usar una imagen base de nginx
FROM nginx:alpine

# Copiar los archivos estáticos HTML/JS/CSS al contenedor de nginx
COPY *.* /usr/share/nginx/html

# Exponer el puerto para el servidor web
EXPOSE 80

# No es necesario especificar un CMD porque el contenedor de nginx ya tiene uno por defecto para iniciar el servidor