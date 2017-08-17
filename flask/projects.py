import os
import simplekml
import time


def sendLogos(lg_IP, lg_Pass, server_IP, proj_name):
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
    screen.size.x = 0.20
    screen.size.y = 0.15
    screen.size.xunits = simplekml.Units.fraction
    screen.size.yunits = simplekml.Units.fraction

    screenName = kml.newscreenoverlay(name='App name')
    screenName.icon.href = "http://" + server_IP + ":5000/logos/" + proj_name + ".png?a=" + \
        str(millis)
    screenName.overlayxy = simplekml.OverlayXY(x=0.0, y=1.0, xunits=simplekml.Units.fraction,
                                               yunits=simplekml.Units.fraction)
    screenName.screenxy = simplekml.ScreenXY(x=0.3, y=0.95, xunits=simplekml.Units.fraction,
                                             yunits=simplekml.Units.fraction)
    screenName.rotationxy = simplekml.RotationXY(x=0.0, y=0.0, xunits=simplekml.Units.fraction,
                                                 yunits=simplekml.Units.fraction)
    screenName.size.x = 0.50
    screenName.size.y = 0.07
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
    command = "echo 'http://" + server_IP + ":5000/logos/Layout.kml?a=" + str(millis) +\
        "' | sshpass -p " + lg_Pass + " ssh lg@" + lg_IP + \
        " 'cat - > /var/www/html/kmls_4.txt'"
    os.system(command)


def floybd(lg_IP, lg_Pass, server_IP):
    sendLogos(str(lg_IP), 'lqgalaxy', str(server_IP), "FlOYBD")
    #os.system('bash /home/lg/Desktop/lglab/gsoc17/FlOYBD/startDjango.sh ' + lg_IP)
    return "FlOYBD"


def memories(lg_IP, lg_Pass, server_IP):
    sendLogos(str(lg_IP), 'lqgalaxy', str(server_IP), "memories")
    return "memories"


def WikimediaDataProject(lg_IP, lg_pass, server_IP):
    sendLogos(str(lg_IP), 'lqgalaxy', str(server_IP), "WikimediaDataProject")
    os.system(
        'bash /home/lg/Desktop/lglab/gsoc17/WikimediaDataProject/WDLG-Start ' + lg_IP)
    return "WikimediaDataProject"


def my_meteorological_station(lg_IP, lg_pass, server_IP):
    sendLogos(str(lg_IP), 'lqgalaxy', str(
        server_IP), "my_meteorological_station")
    return "my_meteorological_station"


def SmartAgroVisualizationTool(lg_IP, lg_pass, server_IP):
    sendLogos(str(lg_IP), 'lqgalaxy', str(
        server_IP), "SmartAgroVisualizationTool")
    return "SmartAgroVisualizationTool"
