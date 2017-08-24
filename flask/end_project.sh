#!/bin/bash
pids=($(ps ax | grep $1| awk '{print $1}'))
for pid in "${pids[@]}"
do
    echo "killing proces "$pid 
    kill $pid
done
echo "" | sshpass -p lqgalaxy ssh lg@$1 'cat - > /var/www/html/kmls.txt'
echo 'search=" "' | sshpass -p lqgalaxy ssh lg@$1 'cat - > /tmp/query.txt'
