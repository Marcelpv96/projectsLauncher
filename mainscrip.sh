proj_name=""
serverip=`ifconfig | grep "inet addr:10" | awk '{print $2}'| cut -d ':' -f 2`
read -p "Which project would you like to start? " proj_name
curl "http://$serverip:5000/project?name=$proj_name&lgip=10.160.67.206&serverip=$serverip"

