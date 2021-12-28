from django.urls import path,include
from .auth import CustomAuthToken
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
    path("Classattone", views.CheckAttOne, name= "ClassAttOne"),

    #path('stuinfo/<int:pk>', views.Student_details),
    #path('student_api/', views.student_api),
    #path('student_api_new/', views.hello_world),
    path('class_api/', views.StudentListAPI.as_view(), name="classall"),
    path('class_api/<int:pk>', views.StudentRetrieveAPI.as_view(), name="classall_sp"),
    path('create_api/', views.StudentCreateAPI.as_view(), name="class_create"),
    path('class_update/<int:pk>', views.StudentUpdateAPI.as_view(), name="class_update"),
    path('class_des/<int:pk>', views.StudentDestroyAPI.as_view(), name="class_des"),
    path('class_listCreate/', views.StudentListCreateAPI.as_view(), name="classListCreate"),
    path('class_RUD/<int:pk>', views.StudentRetrieveUpdateDestroyAPIView.as_view(), name="RUD"),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', CustomAuthToken.as_view())

 
    #path('', views.function2, name="main_route")
]