from flask import Flask, request

app = Flask(__name__)


@app.route('/project', methods=['GET', 'POST'])
def project():
    username = request.args.get('name')
    lgIP = request.args.get('lgip')


if __name__ == "__main__":
    app.run()
