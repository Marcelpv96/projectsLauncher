from flask import Flask, request
from projects import *
from demos import *
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
    proj_name = res["result"]["metadata"]["intentName"]
    tour = res["result"]["parameters"]["tourType"]
    try:
        proj_demos[proj_name](tour)
        return ""
    except KeyError:
        return "ERROR in project NAME"


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


proj_demos = {'floybd': floybd_demo,
              'memories': memories_demo,
              'WikimediaDataProject': WikimediaDataProject_demo,
              'my_meteorological_station': my_meteorological_station_demo,
              'SmartAgroVisualizationTool': SmartAgroVisualizationTool_demo}


if __name__ == "__main__":
    # print proj_demos
    app.run('0.0.0.0')
