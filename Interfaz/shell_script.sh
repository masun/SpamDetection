#!/bin/sh
#while true ; do
#      python manage.py runserver;
#      sleep 2;
#      fuser -k 8000/tcp;
      #ps aux | grep -i manage;

      #pkill manage.py;
      #ps aux | grep -i manage;
#done

ps cax | python manage.py runserver > /dev/null
if [ $? -eq 0 ]; then
  echo "Process is running." &
  echo $!
fi
