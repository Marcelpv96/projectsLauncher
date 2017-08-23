import time
import subprocess

"""
ip = server ip
lg_Ip = liquid galaxy ip
"""
ip = ""
lg_ip = ""


def floybd_demo(tour):
    print " la ip es: " + ip
    port = ":8000"
    link = "curl " + ip + port + tour
    print link
    subprocess.Popen(link, shell=True)
    return "Ok, now FlOYBD demo is launching."


def memories_demo(tour):
    millis = int(round(time.time() * 1000))
    command = "echo 'http://" + ip + ":5000/logos/earth.kml?a=" + str(millis) +\
        "' | sshpass -p lqgalaxy ssh lg@" + lg_ip + \
        " 'cat - > /var/www/html/kmls.txt' "
    print command
    proces = subprocess.Popen(command, shell=True)
    proces.communicate()
    playTour("main")
    return "Ok, now Geographical memories, demo is launching."


def WikimediaDataProject_demo(tour):
    port = ":8000"
    link = "curl " + ip + port
    proces = subprocess.Popen(link + "/try_demo", shell=True)
    proces.communicate()
    print link + tour
    subprocess.Popen(link + tour, shell=True)
    return "Ok, now ,Wiki media data project, demo is launched."


def my_meteorological_station_demo():
    pass


def SmartAgroVisualizationTool_demo():
    link = "curl -X POST" + ip + ":3003" + "/demos/sensors"
    return "Ok, now SAVT , demo is launching."


def StopTour(tour):
    command = "echo 'exittour=true' | sshpass -p lqgalaxy ssh lg@" + \
        lg_ip + " 'cat - > /tmp/query.txt'"
    p1 = subprocess.Popen(command, shell=True)
    p1.communicate()
    for i in xrange(1, 7):
        command2 = "echo '' | sshpass -p lqgalaxy ssh lg@" + lg_ip + " 'cat - > /var/www/html/kmls_" + \
            str(i) + ".txt"
        subprocess.Popen(command2, shell=True)
    return "Ok, now demo is stopped."

def playTour(tourName):
    command = "echo 'playtour="+tourName+"' | sshpass -p lqgalaxy ssh lg@" + lg_ip + \
              " 'cat - > /tmp/query.txt'"
    print command
    subprocess.Popen(command, shell=True)