from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from .views import login,master,index,calib,output,inward,report,invoice,keyboard


urlpatterns = [
    path('',login,name="login"),
    path('index/',index,name="index"),
    path('master/',master,name="master"),
    path('calib/',calib,name="calib"),
    path('output/',output,name="output"),
    path('inward/',inward,name="inward"),
    path('report/',report,name="report"),
    path('invoice/',invoice,name="invoice"),
    path('keyboard/',keyboard,name="keyboard"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)