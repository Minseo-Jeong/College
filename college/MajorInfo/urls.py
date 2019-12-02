from django.urls import path
from MajorInfo import views

urlpatterns = [
    path('', views.MainView.as_view(), name='MainView'),
    # path('', views.Test, name='MainView'),
]
