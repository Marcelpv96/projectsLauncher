#!/bin/bash
bash /flask/end_project.sh manage.py
for i in `seq 1 7`;
       do
               echo "" | sshpass -p lq ssh lg@$1 cat - > /var/www/html/kmls_$i.txt
       done
