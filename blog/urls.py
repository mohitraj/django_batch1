from django.urls import path

from . import views 

urlpatterns = [
    
    path('home',views.home, name="blog_home"),
    path('posts',views.all_post, name="blog_all_post"),
    #path('', views.function2, name="main_route")
]
