from flask import Flask, request, jsonify 
import json 

app = Flask(__name__) 
port = '5000' 

@app.route('/', methods=['POST']) 
def index(): 
  data = json.loads(request.get_data()) 
  print(data)
  date = data['conversation']['memory']['date']['formatted']
  return jsonify( 
    status=200, 
    replies=[{ 
      'type': 'text', 
      'content': "Je note donc un rendez vous pour {}.".format(date), 
    }]
  ) 
 
@app.route('/errors', methods=['POST']) 
def errors(): 
  print(json.loads(request.get_data())) 
  return jsonify(status=200) 
 
app.run(port=port)
