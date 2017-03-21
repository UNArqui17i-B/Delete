from flask import Flask
from flask_restful import Api, Resource
from resource.Delete_Resource import Delete_Resource

app = Flask(__name__,static_folder="static");
api = Api(app)

api.add_resource(Delete_Resource,"/delete/<string:id>")

@app.route("/")
def hello_docker():
    return "Hello DOCKER"

if __name__ == "__main__":
    app.debug = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host="0.0.0.0",port=4030)
