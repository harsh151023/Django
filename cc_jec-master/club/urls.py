"""club URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from c_app import views


urlpatterns = [
    url(r'^$', views.front_page,name = 'front_page'),
    url(r'^about_page/', include('c_app.urls')),
    url(r'^join_page/join', include('c_app.urls')),
    url(r'^front_page/xyz', views.front_page,name = 'front_page'),
    url(r'^front_page/front/', include('c_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^event_page/event1', include('c_app.urls')),



]
