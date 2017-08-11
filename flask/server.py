from flask import Flask, request
from floyd import floyd
app = Flask(__name__,
            static_url_path='',
            static_folder='FlOYD/static')


@app.route('/FlOYD/static/img/propis.png', methods=['GET'])
def staticPropis():
    return app.send_static_file('img/propis.png')


@app.route('/FlOYD/static/img/comuns.png', methods=['GET'])
def staticComuns():
    return app.send_static_file('img/comuns.png')


@app.route('/FlOYD/static/img/logoFloybd.png', methods=['GET'])
def staticLogo():
    return app.send_static_file('img/logoFloybd.png')


@app.route('/FlOYD/static/logos/Layout.kml', methods=['GET'])
def staticLayout():
    return app.send_static_file('logos/Layout.kml')


@app.route('/project', methods=['GET'])
def project():
    proj_name = request.args.get('name')
    lg_IP = request.args.get('lgip')
    try:
        returned = proj_func[proj_name](lg_IP, 'lqgalaxy')
        return returned
    except KeyError:
        return "ERROR in project NAME"


proj_func = {'floyd': floyd}
if __name__ == "__main__":
    app.run('0.0.0.0')
