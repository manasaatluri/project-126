from flask import Flask, jsonify, request
from flask_cors import CORS
  


app = Flask(__name__)
CORS(app) 



m=[
    {
        "name":"vidhushi",
        "age":"13",
        "grade":"9th",
        "height":"149cm"    
    },
    {
        "name":"harsha",
        "age":"14",
        "grade":"9th",
        "height":"172cm"
    },
    {
        "name":"manasa",
        "age":"14",
        "grade":"9th",
        "height":"162cm"
    },
    {
        "name":"navya",
        "age":"15",
        "grade":"9th",
        "height":"169cm"
    }
]

@app.route("/vmh")
def hola():
    return jsonify({
        "data": m,
        "status":"bff"
    })








if __name__ == "__main__":
    app.run()