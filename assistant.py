from flask import Flask, request, jsonify 
import json 
import datetime as dt
import dateutil.parser
import dateutil.tz

import check_calendar

app = Flask(__name__) 
port = '5000' 

@app.route('/', methods=['POST']) 
def index(): 
  data = json.loads(request.get_data()) 
  print(data)
  date = data['conversation']['memory']['date']['formatted']
  date_iso = data['conversation']['memory']['date']['iso']
  date_iso = dateutil.parser.parse(date_iso)
  local = dateutil.tz.tzlocal()
  date_iso = date_iso.replace(tzinfo=local)
  if check_calendar.event_exists_at(date_iso):
      reply = "Désolé, M. Jauzion n'est pas dispo sur ce créneau ({})".format(date_iso)
  else:
      reply = "Je note donc un rendez vous pour {}.".format(date_iso)
  return jsonify( 
    status=200, 
    replies=[{ 
      'type': 'text', 
      'content': reply, 
    }]
  ) 
 
@app.route('/errors', methods=['POST']) 
def errors(): 
  print(json.loads(request.get_data())) 
  return jsonify(status=200) 
 
app.run(port=port)
