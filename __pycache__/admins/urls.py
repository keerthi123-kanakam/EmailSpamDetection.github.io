from django.urls import path 
from . import views
urlpatterns = [
    path('adminhome/', views.adminHome, name='adminHome'),
    path('adminlogin/', views.adminLogin, name='adminLogin'),
    path('adminhomepage/', views.adminHomePage, name='adminHomePage'),
    #path('viewuser/', views.viewUser, name='viewUser'),
    path('show/', views.show, name='show'),
    path('showtweets/', views.showTweets, name='showTweets'),
    path('shownotstresstweets/', views.showNotStressTweets, name='showNotStressTweets'),
    path('stressgraph/', views.stressGraph, name='stressGraph'),
    path('notstressgraph/', views.notStressGraph, name='notStressGraph'),
    path('adminmessage/', views.adminmessage, name='adminmessage'),
    path('adminmessagehtml/(?P<id>\d+)/(?P<userid>\d+)', views.adminmessagehtml, name='adminmessagehtml'),
    path('adminmessagesave/', views.adminmessagesave, name='adminmessagesave'),
]