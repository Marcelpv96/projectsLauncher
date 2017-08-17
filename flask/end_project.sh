#!/bin/bash
pids=($(ps -e | grep $1| awk '{print $1}'))
for pid in "${pids[@]}"
do
    kill $pid
done
