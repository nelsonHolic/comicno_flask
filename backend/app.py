from flask import Flask
from api import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)

def start():
    app.run("0.0.0.0", 5000, debug=True)

if __name__ == '__main__':
    start()