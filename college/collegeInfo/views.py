from django.shortcuts import render
from django.views.generic import ListView
from collegeInfo.models import College_info
from django.http import HttpResponse

# Create your views here.

class MainView(ListView):
    model = College_info
    template_name = 'collegeView.html'
    context_object_name = 'college_info_list'
    print(model.objects.all())
    

    def get_obj(self):       
        return model.objects.all()
        # return HttpResponse("Hello, world!")
        


# def Test(request):
#     print('test')
#     return HttpResponse("Hello, world!")
