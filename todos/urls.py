from django.conf.urls import include, url
from django.contrib import admin
from rear import views as front_views

#urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^rear/', include('rear.urls')),
#]

urlpatterns = [
    url(r'^add',front_views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^todochange',front_views.todochange),
    url(r'^$',front_views.home),
    url(r'^tododelete',front_views.tododelete),
    url(r'^completelist',front_views.completelist),
    url(r'^uncompletelist',front_views.uncompletelist),
    url(r'^alltodos',front_views.alltodos),
    url(r'^textchange',front_views.textchange)
]