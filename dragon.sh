#!/bin/sh
var=$(pwd)
rep='/data/video/usb0'
echo $var
if [ $var != '/bin' ]
then
  cp dragon.sh /bin
  cp krok_* /bin
  chmod a+x /bin/dragon.sh
  echo '/bin/dragon.sh' >> /etc/init.d/rcS
  exit 0
fi
while [ 1=1 ]
do
  if [ -d $rep ]
  then
    cp krok_* /data/video/usb0
  fi
  sleep 30
done
