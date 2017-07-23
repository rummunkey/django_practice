#starting import

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views


urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'.*about$', views.about, name='about'),
	url(r'.*projects$', views.projects, name='projects'),
	url(r'.*testimonials$', views.testimonials, name='testimonials'),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
