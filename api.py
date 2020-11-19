from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import os
from db.dbfunctions import *

app = Flask(__name__)
api = Api(app)
CORS(app)

class ClassResult(Resource):
    def get(self, name):
        db_path = os.path.dirname(os.path.abspath(__file__)) + '\\app\\database.db'
        all_info = get_all_info_structured(db_path)
        descriptions = all_info['descriptions']
        description = descriptions[name]
        if name == 'fighter':
            color = '#6E5841'
        elif name == 'bard':
            color = '#C94DDA'
        elif name == 'barbarian':
            color = '#B43327'
        elif name == 'druid':
            color = '#4AB427'
        elif name == 'wizard':
            color = '#2771B4'
        elif name == 'rogue':
            color = '#434C54'
        elif name == 'cleric':
            color = '#B4AF27'
        elif name == 'monk':
            color = '#C8CA65'
        elif name == 'sorcerer':
            color = '#F96226'
        elif name == 'paladin':
            color = '#F2D826'
        else:
            color = 'black'


        vara = {'classe':name,
                'color':color,
                'description':description,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                }
                };
        return vara

api.add_resource(ClassResult, '/api/result/<name>')



if __name__ == '__main__':
 app.run(debug=True,port="5050")
