from django.urls import path
from . import views

urlpatterns = [
    path('chat/',views.home,name='home'),
    path('checkview',views.checkview,name='checkview'),
    path('<str:room>/',views.roompage,name='roompage'),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),
    path('sample',views.sample,name='sample'),
    path('send',views.send,name='send'),
    path('about',views.about,name='about'),
]
