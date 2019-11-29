import json
import requests

data = requests.get('http://hangang.dkserver.wo.tc/')
data = data.json()
data['temp'] #한강 수온