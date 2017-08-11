import os
import simplekml
import time


def sendLogos(lg_IP, lg_Pass, server_IP):
    millis = int(round(time.time() * 1000))

    kml = simplekml.Kml(name="Layout")
    screen = kml.newscreenoverlay(name='FLOYBD')
    screen.icon.href = "http://" + \
        server_IP + ":5000/FlOYD/static/img/propis.png?a=" + str(millis)
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
    screenName.icon.href = "http://" + \
        server_IP + ":5000/FlOYD/static/img/logoFloybd.png?a=" + \
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
    screen1.icon.href = "http://" + \
        server_IP + ":5000/FlOYD/static/img/comuns.png?a=" + str(millis)
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
    dir1 = os.path.join(currentDir, "/FlOYD/static/logos")
    print dir1
    dirPath2 = os.path.join(dir1, fileName)
    dirPathFinal = currentDir + dirPath2

    kml.save(currentDir + dirPath2)
    command = "echo 'http://" + server_IP + ":5000/FlOYD/static/logos/Layout.kml?a=" + str(millis) +\
        "' | sshpass -p " + lg_Pass + " ssh lg@" + lg_IP + \
        " 'cat - > /var/www/html/kmls_4.txt'"
    os.system(command)


def run():
    pass


def floyd(lg_IP, lg_Pass):
    sendLogos('10.160.67.206', 'lqgalaxy', "10.160.67.51")
    return "TEST"
