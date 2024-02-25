from django.urls import path
from . import views

urlpatterns = [
    path('',views.demo),
    path('entries/<pk>',views.entries),
    # path('web3',views.test)
]