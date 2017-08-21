proj_name="$1"
lgip="$2"
ssh-keyscan -H $lgip >> ~/.ssh/known_hosts
serverip=`ifconfig | grep "inet addr:10" | awk '{print $2}'| cut -d ':' -f 2`
curl "http://$serverip:5000/project?name=$proj_name&lgip=$lgip&serverip=$serverip"
subprocess.Popen("ifconfig | grep inet addr:10 | awk '{print $2}'| cut -d ':' -f 2", shell=True)
