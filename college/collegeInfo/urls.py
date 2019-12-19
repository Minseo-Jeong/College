from django.urls import path
from collegeInfo import views

urlpatterns = [
    path('', views.MainView.as_view(), name='MainView'),
]
