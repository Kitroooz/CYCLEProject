"""
URL configuration for CYCLEdjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from CYCLEapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', cycle, name="cycle"),
    path('admin/', admin.site.urls),
    path('cycle/', cycle, name="cycle"),
    path('index/', index, name="index"),
    path('bikes/', bikes, name="bikes"),
    path('bike/', bike, name="bike"),
    path('buy/', buy, name="buy"),
    path('buy2/', buy2, name="buy2"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
