from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name='home'),
    path('sendplain',views.sendEmail,name='sendEmail'),
    path('sendAttachment',views.sendEmailAttachment,name='sendAttach'),
]