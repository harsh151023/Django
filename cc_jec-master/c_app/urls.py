from django.conf.urls import url
from c_app import views

app_name = 'c_app'

urlpatterns = [
    url(r'^$', views.about_page, name = 'about_page'),
    url(r'^join', views.join_page, name = 'join_page'),
    url(r'^front/', views.front_page, name = 'front_page'),
    url(r'^xyz/', views.front_page, name = 'front_page'),
    url(r'^event1', views.event_page, name = 'event_page'),


]
