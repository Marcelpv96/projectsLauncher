from flask import Flask, request
from floyd import floyd
app = Flask(__name__)


@app.route('/project', methods=['GET'])
def project():
    proj_name = request.args.get('name')
    lg_IP = request.args.get('lgip')
    try:
        proj_func[proj_name](lg_IP, 'lqgalaxy')
        return ""
    except KeyError:
        return "ERROR in project NAME"


proj_func = {'floyd': floyd}
if __name__ == "__main__":

    app.run()
