from django.urls import path

from . import views 

urlpatterns = [
    
    path('home',views.function1),
    path('', views.function2, name="main_route")
]
