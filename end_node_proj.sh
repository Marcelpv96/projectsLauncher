#!/bin/bash
kill -9 $(lsof -i:3000)
kill -9 $(lsof -i:3001)
kill -9 $(lsof -i:3003)
pids=($(ps ax | grep mongo | awk '{print $1}'))
for pid in "${pids[@]}"
do
    echo "killing proces "$pid 
    kill $pid
done
for i in `seq 1 7`;
       do
                kmlfile=kmls_$i.txt
                echo "" | sshpass -p lqgalaxy ssh lg@$1 'cat - > /var/www/html/'$kmlfile
       done
echo "" | sshpass -p lqgalaxy ssh lg@$1 'cat - > /var/www/html/kmls.txt'
echo 'search=" "' | sshpass -p lqgalaxy ssh lg@$1 'cat - > /tmp/query.txt'
