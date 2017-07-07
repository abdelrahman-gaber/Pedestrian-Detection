#!/bin/bash
# This code checks if the matlab license of distributed toolkit is free, then submit a job to nef server
#/opt/matlab2015a/etc/glnxa64/lmutil lmstat -a -c /opt/matlab2015a/licenses/network.lic |grep Users\ of\ Distrib|grep Total\ of\ 0\ licenses\ in\ use

# $? is the exit status of the last executed command.
# For example the command true always returns a status of 0 and false always returns a status of 1
while true
do
  /opt/matlab2015a/etc/glnxa64/lmutil lmstat -a -c /opt/matlab2015a/licenses/network.lic |grep Users\ of\ Distrib|grep Total\ of\ 0\ licenses\ in\ use

  if [ $? -eq 0 ]
  then 
     echo "you can use the licence"
     oarsub -S "$1"
     echo "Job submitted !"
     #mail -s "NEF Job submitted" abdelrahman-gaber.abubakr@inria.fr <<< "Your jub $1 is submitted to NEF GUP .. good luck"

     break
  else
     echo "see you after 30 minutes :3"
     sleep 1800  # in seconds 
  fi

done

echo "Code finished !"

