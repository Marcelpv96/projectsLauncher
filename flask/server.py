from flask import Flask, request, make_response
from projects import *
from demos import *
import projects
import demos
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
    try:
        tour = res["result"]["parameters"]["tourType"]
        print tour
        answer = createWebhookAnswer(proj_demos[tour](tour))
        answer = json.dumps(answer, indent=4)
        return make_response(answer)
    except KeyError:
        return ""


@app.route('/project', methods=['GET'])
def project():
    proj_name = request.args.get('name')
    lg_IP = request.args.get('lgip')
    server_IP = request.args.get('serverip')
    demos.ip = server_IP
    demos.lg_ip = lg_IP
    projects.lg_ip = lg_IP
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


proj_demos = {'/demoLastWeekEarthquakes': floybd_demo,
              '/launchdemogtfs': floybd_demo,
              '/dummyWeather': floybd_demo,
              '/start_barcelona92' :WikimediaDataProject_demo,
              '/savtSensors': SmartAgroVisualizationTool_demo_sensors,
              '/start_lleida_tour': WikimediaDataProject_demo,
              '/overlays': SmartAgroVisualizationTool_demo_overlays,
              'memories': memories_demo,
              '/start_bayern_tour': WikimediaDataProject_demo,
              'my_meteorological_station': my_meteorological_station_demo,
              'StopTour': StopTour}


if __name__ == "__main__":
    # print proj_demos
    app.run('0.0.0.0')
