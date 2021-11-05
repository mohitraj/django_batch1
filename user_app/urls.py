from django.urls import path

from . import views 


urlpatterns = [
    

    path('changepass/', views.UserChangePass, name="ChangePassword"),
    path('upprofile/', views.UpdateProfile, name = 'upprofile')
    #path('', views.function2, name="main_route")
] 

