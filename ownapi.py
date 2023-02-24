from flask import Flask, jsonify

app = Flask(__name__)

information = [
    { "my_details": 
        [
            {    
                "firstName" : "Varun",
                "lastName": "Kumar",
                "Role": "IDCS Systems Engineer",
                "age": 25,
                "colleges went": [
                    {
                        "Name": "Rutgers University",
                        "Year": 2022,
                        "Degree": "Bachelor in Computer Science",
                    },
                    {
                        "Name": "Middlesex County College",
                        "Year": 2020,
                        "Degree": "Associates in Computer Science",
                    }
                ]
            }
        ]
    }
]

@app.route('/')
def index():
    return " This is my API"

@app.route('/information', methods=['GET'])
def get():
    return jsonify({'Information': information})

def create_app():
    return app

if __name__ == "__main__":
    app.run(debug= True, port= 8080)
