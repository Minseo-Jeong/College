from django.views.generic.base import TemplateView
# from django.shortcuts import get_object_or_404, render
from datetime import datetime, timedelta
import json
import requests

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        data = requests.get('http://hangang.dkserver.wo.tc/')
        data = data.json()['temp']

        time1 = datetime(2020, 11, 19, 0, 0, 0)
        time2 = datetime.now()

        context['temp'] = data
        context['dday'] = (time1-time2).days
        print(context)
        return context #한강 수온 float





