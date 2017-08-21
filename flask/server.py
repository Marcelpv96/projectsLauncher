from flask import Flask, request
from projects import *
import json
import subprocess
import time
app = Flask(__name__,
            static_url_path='',
            static_folder='logos')


def createWebhookAnswer(answer):
    return {
        "speech": answer,
        "displayText": answer,
        "source": "API.AI-GSOC-launcherProejcts"
    }


@app.route("/logos/<logo_name>")
def logos(logo_name):
    return app.send_static_file(logo_name)


@app.route("/webhook", methods=['POST'])
def webhook():
    res = request.get_json(silent=True, force=True)
    link = "curl 10.160.67.49:8000"
    project = res["result"]["metadata"]["intentName"]
    tour = res["result"]["parameters"]["tourType"]
    print project
    if project == "WikimediaDataProject":
        print "hola"
        subprocess.Popen(link + "/try_demo", shell=True)
        time.sleep(2)
    subprocess.Popen(link + proj_demos[project][tour], shell=True)
    return ""


@app.route('/project', methods=['GET'])
def project():
    proj_name = request.args.get('name')
    lg_IP = request.args.get('lgip')
    server_IP = request.args.get('serverip')
    try:
        returned = proj_func[proj_name](lg_IP, 'lqgalaxy', server_IP)
        return returned
    except KeyError:
        return "ERROR in project NAME"


proj_func = {'floybd': floybd,
             'memories': memories,
             'WikimediaDataProject': WikimediaDataProject,
             'my_meteorological_station': my_meteorological_station,
             'SmartAgroVisualizationTool': SmartAgroVisualizationTool}

WikimediaDataProject_demos = {'main': '/try_demo',
                              'lleida': '/start_lleida_tour',
                              'bayern': '/start_bayern_tour'}

floybd_demos = {'gtfs': '/launchdemogtfs',
                'LastWeekEarthquakes': '/demoLastWeekEarthquakes',
                'LastWeekEarthquakesHeatmap': '/LastWeekEarthquakesHeatmap',
                'dummyWeather': '/dummyWeather',
                'currentWeather': '/currentWeather'}

proj_demos = {'floybd': floybd_demos,
              'memories': {},
              'WikimediaDataProject': WikimediaDataProject_demos,
              'my_meteorological_station': {},
              'SmartAgroVisualizationTool': {}}

if __name__ == "__main__":
    # print proj_demos
    app.run('0.0.0.0')
