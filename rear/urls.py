from django.conf.urls import include, url
from . import views 
from rear import views as front_views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^api/todos',front_views.todo),
    #url(r'^api/todo/(?P<id>\d+)$',front_views.edit_todo),
    #url(r'^$',front_views.home),
    url(r'^admin/', include(admin.site.urls)),
]