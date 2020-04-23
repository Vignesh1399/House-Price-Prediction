from django.urls import path, re_path
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	re_path(r'^$', views.get_prediction, name='get_prediction'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


