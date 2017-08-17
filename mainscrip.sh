proj_name="$1"
lgip="$2"
serverip=`ifconfig | grep "inet addr:10" | awk '{print $2}'| cut -d ':' -f 2`
curl "http://$serverip:5000/project?name=$proj_name&lgip=$lgip&serverip=10.160.67.239"
