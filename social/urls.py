from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login',views.loginpage,name='loginpage'),
    path('logout',views.logoutpage,name='logoutpage'),
    path('signup',views.signuppage,name='signup'),
    path('settings',views.settings,name='settings'),
    path('upload',views.upload,name='upload'),
    path('uploadstang',views.uploadstang,name='uploadstang'),
    path('profile/<str:user>',views.viewprofile,name='viewprofile'),
    path('followupdate',views.followupdate,name='followupdate'),
    path('likepost',views.likepost,name='likepost'),
    path('likestang',views.likestang,name='likestang'),
    path('deletepost',views.deletepost,name='deletepost'),
    path('deletestang',views.deletestang,name='deletestang'),
    path('search',views.search,name='search'),
    path('uploadvideo',views.uploadvideo,name='uploadvideo'),
]
