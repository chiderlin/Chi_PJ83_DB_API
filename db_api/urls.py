"""PJ83_db_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from db_api import views

urlpatterns = [ 
    # DomainTestLog
    path('domaintestlog/c/', views.C_data_DomainTestLog, name="C_data_DomainTestLog"),
    path('domaintestlog/r/', views.R_data_DomainTestLog, name="R_data_DomainTestLog"),
    url(r'^domaintestlog/u/(\d+)/$', views.U_data_DomainTestLog, name="U_data_DomainTestLog"),
    url(r'^domaintestlog/d/(\d+)/$', views.D_data_DomainTestLog, name="D_data_DomainTestLog"),
    path('domaintestlog/d/all/', views.D_all_data_DomainTestLog, name="D_all_data_DomainTestLog"),


    # DomainListAll
    path('domainlistall/c/', views.C_data_DomainListAll, name="C_data_DomainListAll"),
    path('domainlistall/r/', views.R_data_DomainListAll, name="R_data_DomainListAll"),
    url(r'^domainlistall/u/(\d+)/$', views.U_data_DomainListAll, name="U_data_DomainListAll"),
    url(r'^domainlistall/d/(\d+)/$', views.D_data_DomainListAll, name="D_data_DomainListAll"),
    path('domainlistall/d/all/', views.D_all_data_DomainListAll, name="D_all_data_DomainListAll"),

    # 7zfile
    path('upload/', views.FileView.as_view(), name='upload'),
    # path('upload/', views.upload_file, name="upload_file"),
    # path('download/', views.download_file, name="download_file"),

]

