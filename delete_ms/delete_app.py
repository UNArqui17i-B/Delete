import atexit
import requests
#import logging
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask,url_for,current_app
from flask_restful import Api, Resource
from resource.Delete_Resource import Delete_Resource
from resource.Get_Resource import Get_Resource
from os import environ
from couchdb import Server

app = Flask(__name__,static_folder="static");
api = Api(app)

api.add_resource(Delete_Resource,"/delete/<string:id>")
api.add_resource(Get_Resource,"/delete/get_expiring_files/<int:exp_date>")

scheduler = BackgroundScheduler(timezone=utc)
#logging.basicConfig()

@app.route("/")
def hello_docker():
    print("Hello DOCKER & Delete")
    
#atexit.register(lambda: scheduler.shutdown(wait=False))
#job = scheduler.add_job(hello_docker,'interval', seconds=2)
#scheduler.start()	

if __name__ == "__main__":
    app.debug = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host=environ["HOST_URL"],port=int(environ["HOST_PORT"]))
    #app.run(port=8080)
    