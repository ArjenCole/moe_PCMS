"""SMEDI_CIDataPlatform URL Configuration

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
from DataSite import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^home/', views.home),
    url(r'^register/', views.register),
    url(r'^charts/', views.index),
    url(r'^retrieval/', views.retrieval),
    url(r'^check/', views.check),
    url(r'^upload/', views.upload),
    url(r'^forms/', views.forms),
    url(r'^tables/', views.tables),
    url(r'^login/', views.login),
    url(r'^gantt/', views.gantt),
    url(r'^moe_HOME/', views.moe_HOME),
    url(r'^moe_investment_estimate/', views.moe_investment_estimate),
    url(r'^moe_Tender_offer/', views.moe_Tender_offer),
    url(r'^moe_Tender_offer_diff/', views.moe_Tender_offer_diff),
    url(r'^moe_Tender_offer_diff_analysis/', views.moe_Tender_offer_diff_analysis),
    url(r'^moe_Tender_offer_risk/', views.moe_Tender_offer_risk),
    url(r'^moe_Controlled_price/', views.moe_Controlled_price),
    url(r'^moe_Controlled_price_diff/', views.moe_Controlled_price_diff),
    url(r'^moe_Controlled_price_analysis/', views.moe_Controlled_price_analysis),
    url(r'^moe_Monthly_report_analysis/', views.moe_Monthly_report_analysis),
    url('', views.login),# views.login
]



