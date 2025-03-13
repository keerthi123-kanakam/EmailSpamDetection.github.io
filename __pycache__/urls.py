from django.urls import path 
from . import views
urlpatterns = [
	path('home/', views.home, name='home'),
	path('post/', views.post_new, name='post_new'),
	path("registration/", views.registration, name="registration"),
	path("userlogincheck/", views.userLoginCheck, name="userLoginCheck"),
	path("userhome/", views.userHome, name="userHome"),
	path("tweeets/", views.tweet, name="tweet"),
	path("chart_page/(?P<chart_type>\w+)", views.chart_page, name="chart_page"),
	path("chart_page1/(?P<chart_type>\w+)", views.chart_page1, name="chart_page1"),
	path("sentitems/", views.sentitems, name="sentitems"),
	path("inbox/", views.inbox, name="inbox"),
	path("phishingtweet/", views.phishingtweet, name="phishingtweet"),
	path("usermessage/", views.usermessage, name="usermessage"),
	path("usermessagesave/", views.usermessagesave, name="usermessagesave"),
	path('adminmessagereply/', views.adminmessagereply, name='adminmessagereply'),
	path('nb/', views.nb, name='nb'),
	path('svc/', views.svc, name='svc'),
	path("new_job/(?P<id>\d+)", views.new_job, name="new_job"),
	path("retrieveEmployee/", views.retrieveEmployee, name="retrieveEmployee"),
	path("retrieveSingleRecord/", views.retrieveSingleRecord, name="retrieveSingleRecord"),
	path("updateRecord/", views.updateRecord, name="updateRecord"),
	path("employee/", views.employee, name="employee"),
	path("employeeFilterMethod/", views.employeeFilterMethod, name="employeeFilterMethod"),
	path("employeeOB/", views.employeeOB, name="employeeOB"),
	path("employeefiltOB/", views.employeefiltOB, name="employeefiltOB"),
	path("delet/", views.delet, name="delet")
]