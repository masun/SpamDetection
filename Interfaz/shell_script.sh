#!/bin/sh

# Para el 'correcto' funcionamiento de la aplicación.
fuser -k 8080/tcp; # Se mata el proceso que esté usando el puerto 8080.
sleep 1;           # Se espera un segundo para activar el servidor.
python manage.py runserver 0.0.0.0:8080; # Se inicia el servidor de Django

while true ; do
    if lsof -Pi :8080 -sTCP:LISTEN -t >/dev/null ; then
        echo "Running Django"
    else
        echo "Start Django"
        python manage.py runserver 0.0.0.0:8080;
    fi
done
