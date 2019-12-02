from django.shortcuts import render
from django.views.generic import ListView
from MajorInfo.models import Major_info
from django.http import HttpResponse

# Create your views here.

class MainView(ListView):
    model = Major_info
    template_name = 'MajorView.html'
    context_object_name = 'major_info_list'
    print(model.objects.all())

    def get_obj(self):       
        return model.objects.all()
        # return HttpResponse("Hello, world!")


# def Test(request):
#     print('test')
#     return HttpResponse("Hello, world!")
