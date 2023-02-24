from flask import Flask
import json
from pprint import pprint as pp
import time

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    data = {
                'Name' : 'Varun Kumar', 
                'Message': 'My Information',
                'Timestamp': time.time(),
                'Age' : 25,
                'Academic Experience': 
                    [
                        {    
                            "Colleges" :[
                                {
                                    "Name" : "Rutgers University",
                                    "Year" : 2022,
                                    "Degree" : "Bachelor's in Computer Science",
                                    "Graduated" : True
                                },
                                {
                                    "Name" : "MiddleSex County College",
                                    "Year" : 2020,
                                    "Degree" : "Associate's's in Computer Science",
                                    "Graduated" : True
                                }
                                ]
                            }
                    ],
                    'Work Experience' : 
                    [
                            {
                                    "Company" : "SHI international corp",
                                    "Role": "IDCS Systems Engineer",
                                    "Started" : "January-7-2023",
                                    "Still Working" : True
                            },
                            {
                                    "Company" : "NJ Transit",
                                    "Role": "Digital Commerce Analyst",
                                    "Started" : "September-26-2022",
                                    "Still Working" : False,
                                    "Ended" : "January-05-2023"
                            },
                            {
                                    "Company" : "NJ Transit",
                                    "Role": "Technical Specialist in Mobile Applications ",
                                    "Started" : "September-26-2022",
                                    "Still Working" : False,
                                    "Ended" : "August-12-2022"
                            }
                    ]            
            }

    jsonData = json.dumps(data)
    return jsonData

@app.route('/user/', methods = ['GET'])
def request():

    user = str(request.args.get('user'))
    data = {
                'Page' : 'Request', 
                'Message': f'Successfully got the request for {user}',
                'Timestamp': time.time()
           }
    jsonData = json.dumps(data)
    return jsonData
    

if __name__ == "__main__":
    app.run(port= 7777)