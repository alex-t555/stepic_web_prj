"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path, include
from django.conf.urls import include, url

from qa import views

urlpatterns = [
    # url(r'^$', include('qa.urls')),
    url(r'^$', view=views.home, name='home'),
    # url(r'^login/', include('qa.urls')),
    url(r'^login/', view=views.login, name="login"),
    url(r'^logout/', view=views.logout, name="logout"),
    # url(r'^signup/', include('qa.urls')),
    url(r'^signup/', view=views.signup, name="signup"),
    # url(r'^question/', include('qa.urls')),
    url(r'^question/(?P<id_question>[0-9]+)/$', view=views.question, name='question'),
    # url(r'^ask/', include('qa.urls')),
    url(r'^ask/', view=views.ask, name='ask'),
    # url(r'^popular/', include('qa.urls')),
    url(r'^popular/', view=views.popular, name='popular'),
    url(r'^new/', include('qa.urls')),
    # path('', include('qa.urls')),
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
]
