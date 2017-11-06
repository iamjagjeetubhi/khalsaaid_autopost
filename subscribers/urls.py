
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^(?P<username>\w+)/$', views.myprofileview, name="detail_profile"),
	url(r'^$', views.subscriber, name='subscriber'),
	url(r'^subscribed', views.subscribed, name='subscribed')
]
