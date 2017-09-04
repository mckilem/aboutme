"""aboutme URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', mainpage, name='home_page'),
    url(r'^study$', studypage, name='study_page'),
    url(r'^work$', workpage, name='work_page'),
    url(r'^work/(?P<id>\d+)$', workpage_detailed, name='work_page_detailed'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
