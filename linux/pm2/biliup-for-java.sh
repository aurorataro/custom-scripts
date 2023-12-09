#!/bin/bash
sudo trickle -s -u 2304 \
java -Dserver.port=2357 -Drecord.work-path=/mnt/Bilirec -Duser.timezone=Asia/Shanghai \
-jar /opt/biliup-for-java/biliupforjava-latest.war
