from django.urls import path,include
from .views import customer,signup

urlpatterns = [
    path('need',customer,name='need'),
    path('signup/',signup,name='signup' ),
]
