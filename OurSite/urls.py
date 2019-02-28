"""OurSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.views.static import serve
from OurSite.settings import MEDIA_ROOT

# 概要
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    # SENPENG
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    #re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#增加此行
    path('forum/',include('article.urls')),

    # WENRONG
    path('account/', include('account.urls')),

    # XIAOPENG
    path('medical/',include('medical.urls')),
    # path('chat/',include('chat.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title='青天游弋后台管理')),
    path('schema/',schema_view),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
