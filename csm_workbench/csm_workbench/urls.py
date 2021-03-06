"""csm_workbench URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include

urlpatterns = [
    #login
    url(r'^auth/', include('login.urls')),
    # homepage
    url(r'^', include('dashboard.urls')),
    url(r'^home/', include('dashboard.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    # business 
    url(r'^cluster/', include('manage_cluster.urls')),
    url(r'^server/', include('manage_server.urls')),
    url(r'^device/', include('manage_device.urls')),
    # csm system
    url(r'^account/', include('manage_account.urls')),
]
