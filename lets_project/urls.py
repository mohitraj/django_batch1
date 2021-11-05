# Base URL project URl
from django.contrib import admin
from django.urls import path, include
from blog1 import views 
from django.contrib.auth import views as auth_views
from user_app import views as user_views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog1.urls') ),
    path('att/',include('attendance.urls') ),
    #path("login/", auth_views.LoginView.as_view(template_name='user_app/login.html'), name= 'login'),
    path("login/", user_views.login_page, name='login'),
    path("signup/", user_views.register, name='register'),

    path("logout/", auth_views.LogoutView.as_view(template_name='user_app/logout.html'), name= 'logout'),

    path("profile/",  user_views.profile, name= 'profile'),
    path('user/',include('user_app.urls') ),

    #path('home/',views.function1),
    #path('', views.function2, name="main_route")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)