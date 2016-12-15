"""GreenLeaf main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user/(\w+)/strains/$', views.strains, name='strains'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^user/(\w+)/logout/$', views.logout_view, name='logout'),
    url(r'^user/(\w+)/upload-strain/$', views.upload_strain, name='upload'),
    url(r'^user/(\w+)/change-banner/$', views.banner_color, name='color'),
    url(r'^user/(\w+)/detail/(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^user/(\w+)/update-page/$', views.update_page, name='update-page'),
    url(r'^user/(\w+)/update-strain/(?P<slug>[\w-]+)/$', views.update_strain, name="update-strain"),
    url(r'^user/(\w+)/delete-strain/$', views.delete_strain, name="delete"),
]

#add to bottom of file
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT })
    ]