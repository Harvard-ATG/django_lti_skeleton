from django.conf.urls import url
from views import MyLTILaunchView
urlpatterns = [
    url(r'^$', 'myapp.views.index', name='index'),
    url(r'^launch$', MyLTILaunchView.as_view(), name='launch'),
    url(r'^hello_world$', 'myapp.views.hello_world', name='hello_world'),
    url(r'^course/(?P<course_id>\d+)$', 'myapp.views.index', name='index'),
]
