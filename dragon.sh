#!/bin/sh

if [[ pwd != "/bin" ]]
then
  cp dragon.sh /bin
  cp krok_* /bin
  chmod a+x /bin/dragon.sh
  echo '/bin/dragon.sh' >> /etc/init.d/rcS
  /bin/dragon.sh
else
  while [ 1==1 ]
  do
    /bin/mount_usb.sh sda
    cp krok_* /data/video/usb1
    /bin/umount_usb.sh sda
    for i in `seq 1 30`;
    do
      sleep 10000000
    done
  done
fi
