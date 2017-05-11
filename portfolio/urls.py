"""portfolio URL Configuration

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

import homepage.views
import blog.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage.views.homepage, name="homepage"),
    url(r'^animals$', homepage.views.animals, name="animals"),
    url(r'^darkside$', homepage.views.darkside, name="darkside"),
    url(r'^meddle$', homepage.views.meddle, name="meddle"),
    url(r'^blog/(\S+)/(\S+)/$', blog.views.blog_post),
    url(r'^blog/(\S+)/$', blog.views.blog_index),
    url(r'^poll/(\S+)/results/$', blog.views.results),
    url(r'^poll/(\S+)/$', blog.views.poll_index),


]
