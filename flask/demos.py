
import subprocess

link = subprocess.check_output(
    "ifconfig | grep 'inet addr:10' | awk '{print $2}'| cut -d ':' -f 2", stderr=subprocess.STDOUT,shell=True)


def floybd_demo(tour):
    port = ":8000"
    print link + port + tour
    subprocess.Popen("curl "+link + port + tour, shell=True)


def memories_demo():
    pass


def WikimediaDataProject_demo(tour):
    port = ":8000"
    print link + tour
    subprocess.Popen("curl "+link + port + "/try_demo", shell=True)
    time.sleep(2)
    subprocess.Popen(link + port + tour, shell=True)


def my_meteorological_station_demo():
    pass


def SmartAgroVisualizationTool_demo():
    pass
