from django.urls import path,include
from user import views
from .views import home,ArticleDetail,AddPost,blog
urlpatterns = [
    path('',home.as_view(),name='home'),
    path('contact', views.contact, name='contact'),
    path('service', views.service,name='service'),
    path('article/<int:pk>/',ArticleDetail.as_view(),name='articledetail'),
    path('post/',AddPost.as_view(),name='add_post'),
    path('blog/',blog.as_view(),name='blog'),


]