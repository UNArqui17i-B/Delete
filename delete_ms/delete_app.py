from flask import Flask,url_for,current_app
from flask_restful import Api, Resource
from resource.Delete_Resource import Delete_Resource
from resource.Delete_Expiring_Resource import Delete_Expiring_Resource
from os import environ

app = Flask(__name__,static_folder="static");
api = Api(app)

api.add_resource(Delete_Resource,"/delete/<string:id>")
api.add_resource(Delete_Expiring_Resource,"/delete_expiring_files/<int:exp_date>")

@app.route("/")
def hello_docker():
    print("Hello DOCKER & Delete")


if __name__ == "__main__":
    app.debug = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host=environ["HOST_URL"],port=int(environ["HOST_PORT"]))
    #app.run(port=8080)
    