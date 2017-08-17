#!/bin/bash
for i in `seq 1 7`;
       do
                kmlfile=kmls_$i.txt
                echo "" | sshpass -p lqgalaxy ssh lg@$1 'cat - > /var/www/html/'$kmlfile
       done
echo "" | sshpass -p lqgalaxy ssh lg@$1 'cat - > /var/www/html/'kmls.txt
