from django.conf.urls import include, url
from django.contrib import admin
from rear import views as front_views

#urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^rear/', include('rear.urls')),
#]

urlpatterns = [
    #url(r'^',front_views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/todos',front_views.todo),
    url(r'^api/todo/(?P<id>\d+)$',front_views.edit_todo),
    #url(r'^todochange',front_views.todochange),
    #url(r'^$',front_views.home)
]
