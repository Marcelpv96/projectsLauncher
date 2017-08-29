import os
import simplekml
import time
import subprocess
lg_ip = ""

def sendLogos(lg_IP, lg_Pass, server_IP, proj_name, xPropi, yPropi, xAgraiments, yAgraiments):
    millis = int(round(time.time() * 1000))
    kml = simplekml.Kml(name="Layout")
    screen = kml.newscreenoverlay(name="FlOYBD")
    screen.icon.href = "http://" + server_IP + \
        ":5000/logos/propis_" + proj_name + ".png?a=" + str(millis)
    screen.overlayxy = simplekml.OverlayXY(x=0.0, y=1.0, xunits=simplekml.Units.fraction,
                                           yunits=simplekml.Units.fraction)
    screen.screenxy = simplekml.ScreenXY(x=0.0, y=1.0, xunits=simplekml.Units.fraction,
                                         yunits=simplekml.Units.fraction)
    screen.rotationxy = simplekml.RotationXY(x=0.0, y=0.0, xunits=simplekml.Units.fraction,
                                             yunits=simplekml.Units.fraction)
    screen.size.x = xAgraiments
    screen.size.y = yAgraiments
    screen.size.xunits = simplekml.Units.fraction
    screen.size.yunits = simplekml.Units.fraction

    screenName = kml.newscreenoverlay(name='App name')
    screenName.icon.href = "http://" + server_IP + ":5000/logos/" + proj_name + ".png?a=" + \
        str(millis)
    screenName.overlayxy = simplekml.OverlayXY(x=0.0, y=1.0, xunits=simplekml.Units.fraction,
                                               yunits=simplekml.Units.fraction)
    screenName.screenxy = simplekml.ScreenXY(x=0.5, y=0.95, xunits=simplekml.Units.fraction,
                                             yunits=simplekml.Units.fraction)
    screenName.rotationxy = simplekml.RotationXY(x=0.0, y=0.0, xunits=simplekml.Units.fraction,
                                                 yunits=simplekml.Units.fraction)
    screenName.size.x = xPropi
    screenName.size.y = yPropi
    screenName.size.xunits = simplekml.Units.fraction
    screenName.size.yunits = simplekml.Units.fraction

    screen1 = kml.newscreenoverlay(name='Logos')
    screen1.icon.href = "http://" + server_IP + \
        ":5000/logos/comuns.png?a=" + str(millis)
    screen1.overlayxy = simplekml.OverlayXY(x=0.0, y=0.0, xunits=simplekml.Units.fraction,
                                            yunits=simplekml.Units.fraction)
    screen1.screenxy = simplekml.ScreenXY(x=0.0, y=0.01, xunits=simplekml.Units.fraction,
                                          yunits=simplekml.Units.fraction)
    screen1.rotationxy = simplekml.RotationXY(x=0.0, y=0.0, xunits=simplekml.Units.fraction,
                                              yunits=simplekml.Units.fraction)
    screen1.size.x = 0.3
    screen1.size.y = 0.25
    screen1.size.xunits = simplekml.Units.fraction
    screen1.size.yunits = simplekml.Units.fraction

    currentDir = os.getcwd()
    print "current dir : " + currentDir

    fileName = "Layout.kml"
    dir1 = os.path.join(currentDir, "/logos")
    print dir1
    dirPath2 = os.path.join(dir1, fileName)
    dirPathFinal = currentDir + dirPath2
    kml.save(currentDir + dirPath2)

    
    getLeftScreenCommand = "sshpass -p " + lg_Pass + " ssh lg@" + lg_IP + \
        " 'head -n 1 personavars.txt | cut -c17-19'"
    leftScreenDirty = subprocess.check_output(
        getLeftScreenCommand, stderr=subprocess.STDOUT, shell=True)
    leftScreenClean = leftScreenDirty.rstrip().decode("utf-8")
   
    leftScreenNumber = leftScreenClean[-1:]
    #leftScreenNumber = "4"

    print leftScreenNumber
    command = "echo 'http://" + server_IP + ":5000/logos/Layout.kml?a=" + str(millis) +\
        "' | sshpass -p " + lg_Pass + " ssh lg@" + lg_IP + \
        " 'cat - > /var/www/html/kmls_" + leftScreenNumber + ".txt' "
    #command = "echo 'abc' > /tmp/a.txt"
    print command
    subprocess.Popen(command, shell=True)
    print 'y'


def floybd(lg_IP, lg_Pass, server_IP):
    sendLogos(str(lg_IP), 'lqgalaxy', str(server_IP), "FlOYBD",
              xPropi=0.50, yPropi=0.07, xAgraiments=0.20, yAgraiments=0.15)
    subprocess.Popen(
        'bash /home/lg/Desktop/lglab/gsoc17/FlOYBD/startDjango.sh ' + lg_IP, shell=True)
    return "FlOYBD"


def memories(lg_IP, lg_Pass, server_IP):
    sendLogos(str(lg_IP), 'lqgalaxy', str(server_IP), "memories",
              xPropi=0.35, yPropi=0.05, xAgraiments=0.20, yAgraiments=0.031)
    return "memories"


def WikimediaDataProject(lg_IP, lg_pass, server_IP):
    print "hola"
    sendLogos(str(lg_IP), 'lqgalaxy', str(server_IP), "WikimediaDataProject",
              xPropi=0.35, yPropi=0.10, xAgraiments=0.25, yAgraiments=0.1)
    subprocess.Popen(
        'bash /home/lg/Desktop/lglab/gsoc17/WikimediaDataProject/WDLG-Start ' + lg_IP, shell=True)
    
    return "WikimediaDataProject"


def my_meteorological_station(lg_IP, lg_pass, server_IP):
    sendLogos(str(lg_IP), 'lqgalaxy', str(
        server_IP), "my_meteorological_station", xPropi=0.35, yPropi=0.10, xAgraiments=0.30, yAgraiments=0.15)
    subprocess.Popen(
        "bash /home/lg/Desktop/lglab/gsoc17/my-meteorological-station/run.sh", shell=True)
    return "my_meteorological_station"


def SmartAgroVisualizationTool(lg_IP, lg_pass, server_IP):
    sendLogos(str(lg_IP), 'lqgalaxy', str(
        server_IP), "SmartAgroVisualizationTool", xPropi=0.32, yPropi=0.15, xAgraiments=0.33, yAgraiments=0.20)
    comand = "mongod --dbpath /home/lg/Desktop/lglab/gsoc17/SmartAgroVisualizationTool/sensor-api/data/db/"
    proc = subprocess.Popen(comand,shell=True)
    
    subprocess.Popen(
        "bash /home/lg/Desktop/lglab/gsoc17/SmartAgroVisualizationTool/run.sh "+lg_ip, shell=True)
    subprocess.Popen(
        "bash /home/lg/Desktop/lglab/gsoc17/SAVT-Dashboard/run.sh", shell=True)
    subprocess.Popen(
        "bash /home/lg/Desktop/lglab/gsoc17/SmartAgroVisualizationTool/sensor-api/run.sh", shell=True)
    return "SmartAgroVisualizationTool"
