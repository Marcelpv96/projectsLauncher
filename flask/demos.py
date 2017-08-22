import time
import subprocess

ip = ""
lg_ip = ""


def floybd_demo(tour):
    print " la ip es: " + ip
    port = ":8000"
    link = "curl " + ip + port + tour
    print link
    subprocess.Popen(link, shell=True)
    return "Ok, now FlOYBD demo is launching."


def memories_demo():
    pass


def WikimediaDataProject_demo(tour):
    port = ":8000"
    link = "curl " + ip + port
    proces = subprocess.Popen(link + "/try_demo", shell=True)
    proces.communicate()
    print link + tour
    subprocess.Popen(link + tour, shell=True)
    return "Ok, now ,Wiki media data project, demo is launching."


def my_meteorological_station_demo():
    return "Ok, now ,Wiki media data project, demo is launching."


def SmartAgroVisualizationTool_demo():
    pass


def StopTour(tour):
    command = "echo 'exittour=true' | sshpass -p lqgalaxy ssh lg@" + \
        lg_ip + " 'cat - > /tmp/query.txt'"
    subprocess.Popen(command, shell=True)
    return "Ok, now demo is stopping."
