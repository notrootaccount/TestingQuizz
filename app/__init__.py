from flask import Flask
from db.initdatabase import init_db
from db.dbfunctions import *
import os
####################   START DB AND VARIABLES #############################
init_db.start_db()
global preguntas
global db_path
global descriptions
db_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\app\\database.db'
all_info = get_all_info_structured(db_path)

preguntas=all_info['questions']
descriptions = all_info['descriptions']




##############################################################################
app = Flask(__name__)
from app import routes
