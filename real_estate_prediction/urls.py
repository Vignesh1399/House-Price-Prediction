"""real_estate_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
import registration
import home


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^registration/', include('registration.urls')),
    re_path(r'^getprediction/', include('home.urls')),
    re_path(r'^showresults/', home.views.HouseList.as_view(), name = 'show_results'),
    re_path(r'^$', registration.views.home_view, name = 'home_view'),
    re_path(r'^', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


