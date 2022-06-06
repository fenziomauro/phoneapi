from django.urls import path
from . import views

urlpatterns =[
    #/phonebook/
    path('', views.IndexView.as_view(), name='index'),
    #/phonebook/add/
    path('add/', views.add, name='addbook'),
    # /phonebook/3/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /phonebook/3/addaddcontact
    path('<int:pk>/addcontact/', views.addcontact, name='addcontact'),

]