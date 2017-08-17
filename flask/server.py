from flask import Flask, request
from projects import *
app = Flask(__name__,
            static_url_path='',
            static_folder='logos')


@app.route("/logos/<logo_name>")
def logos(logo_name):
    return app.send_static_file(logo_name)


@app.route("/webhook")
def webhook():
    pass


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

if __name__ == "__main__":
    app.run('0.0.0.0')
