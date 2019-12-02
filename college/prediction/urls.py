from django.urls import path
from prediction import views

urlpatterns = [
    # path('', views.renew_book_librarian, name='renew-book-librarian'),
    path('', views.Test, name='predictionView'),
    path('post/', views.posttest, name='posttest'),
    
]
