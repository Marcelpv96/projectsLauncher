
import subprocess

link = subprocess.Popen(
    "ifconfig | grep 'inet addr:10' | awk '{print $2}'| cut -d ':' -f 2", shell=True)


def floybd_demo(tour):
    port = ":8000"
    subprocess.Popen(link + port + tour, shell=True)


def memories_demo():
    pass


def WikimediaDataProject_demo(tour):
    port = ":8000"
    print link + tour
    subprocess.Popen(link + port + "/try_demo", shell=True)
    time.sleep(2)
    subprocess.Popen(link + port + tour, shell=True)


def my_meteorological_station_demo():
    pass


def SmartAgroVisualizationTool_demo():
    pass
