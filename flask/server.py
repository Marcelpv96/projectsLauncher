from flask import Flask, request
from projects import *
app = Flask(__name__,
            static_url_path='',
            static_folder='FlOYBD/static')


@app.route('/FLOYBD/static/img/propis.png', methods=['GET'])
def staticPropis():
    return app.send_static_file('img/propis.png')


@app.route('/FLOYBD/static/img/comuns.png', methods=['GET'])
def staticComuns():
    return app.send_static_file('img/comuns.png')


@app.route('/FLOYBD/static/img/logoFloybd.png', methods=['GET'])
def staticLogo():
    return app.send_static_file('img/logoFloybd.png')


@app.route('/FLOYBD/static/logos/Layout.kml', methods=['GET'])
def staticLayout():
    return app.send_static_file('logos/Layout.kml')


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
             'my_meteorological_station': my_meteorological_station}

if __name__ == "__main__":
    app.run('0.0.0.0')
