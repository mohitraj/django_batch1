from django.urls import path

from . import views 

urlpatterns = [
    
    path('postcreate',views.CreatePost, name='blog_createpost'),
    path('allpost',views.AllPost, name='blog_allpost'),
    path('post/new/',views.PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/',views.PostDetailsView.as_view(),name='post-sp'),
    path('post/view/',views.PostListView.as_view(),name='post-all'),
    path('post/<str:username>', views.UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name='post-delete'),

 
    #path('', views.function2, name="main_route")
]
