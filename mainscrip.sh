serverip=ifconfig | grep "inet 10." | awk '{print $2}'
curl http://$serverip:5000/project?name=floybd&lgip=10.160.67.206&serverip=$serverip
