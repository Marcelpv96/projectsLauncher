#!/bin/bash
bash /home/lg/Desktop/lglab/projectsRunner/flask/end_project.sh manage.py
echo $1
for i in `seq 1 7`;
       do
		kmlfile=kmls_$i.txt
		echo "" | sshpass -p lqgalaxy ssh lg@$1 'cat - > /var/www/html/'$kmlfile
       done
echo "" | sshpass -p lqgalaxy ssh lg@$1 'cat - > /var/www/html/kmls.txt'
