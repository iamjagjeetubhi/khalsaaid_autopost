from django.conf.urls import include, url, handler404
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from subscribers import views


from django.contrib.auth import views as auth_views
handler404 = 'subscribers.views.subscriber'


urlpatterns = [
    url(r'^$', views.subscriber, name='subscriber'),
    url(r'^subscribed', views.subscribed, name='subscribed'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
