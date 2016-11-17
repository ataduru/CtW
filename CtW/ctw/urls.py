"""ctw URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'ctw.view.server', name='Server'),
    url(r'^login$', 'ctw.view.login_view', name='Login'),
	url(r'^login/$', 'ctw.view.login_view', name='Login'),
	url(r'^loginp$', 'ctw.view.login_post', name='Loginp'),
	url(r'^signup$', 'ctw.view.sign_up_view', name='Signup'),
	url(r'^signupp$', 'ctw.view.sign_up', name='Signupp'),
	url(r'^command$', 'ctw.view.commands', name='Commands'),
    url(r'^client$', 'ctw.view.client', name='Client'),
    url(r'^harita$', 'ctw.view.updateMap', name='Harita'),
    url(r'^logout$', 'ctw.view.logout_view', name='Logout'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT})

]
