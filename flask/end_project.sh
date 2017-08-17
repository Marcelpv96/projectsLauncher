#!/bin/bash
pids=($(ps ax | grep $1| awk '{print $1}'))
for pid in "${pids[@]}"
do
    echo "killing proces "$pid 
    kill $pid
done
