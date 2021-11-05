from django.urls import path

from . import views 

urlpatterns = [
    
    path('formtest',views.AttView, name="att"),
    path('formtest1',views.AttView1, name="att1"),
    path('mark',views.attstundent, name="mark_att"),
    path('success',views.success, name="success_add"),
    path('checkall',views.checkall, name="checkall"),
    path('checkall/<int:roll>/',views.CheckOne, name= "checkone"),
    path('checkone', views.checkOneform, name= "checkone1"),
    path('masterdata', views.MasterDataEnter, name= "MasterDataEnter"),
    path('markatt', views.MarkAtt, name= "Markatt"),
    path("ClassAtt", views.ClassAttendance, name= "ClassAttendance"),
    path("Classattone", views.CheckAttOne, name= "ClassAttOne")
 
    #path('', views.function2, name="main_route")
]