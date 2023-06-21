"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf 다른 URL.py로 이동하려면 이렇게 해라
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#http://127.0.0.1/
#http://127.0.0.1/app/
#http://127.0.0.1/create/
#http://127.0.0.1/read/1/

urlpatterns = [
    path('admin/', admin.site.urls), #관리자 화면으로 이동하기 위한 기본 라우팅
    path('', include('myapp.urls'))
]
