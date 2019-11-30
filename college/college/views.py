from django.views.generic.base import TemplateView
import json
import requests

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_temp(self):
        data = requests.get('http://hangang.dkserver.wo.tc/')
        data = data.json()
        return data['temp'] #한강 수온 float
