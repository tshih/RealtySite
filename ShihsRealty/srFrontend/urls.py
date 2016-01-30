from django.conf.urls import url

from . import views

app_name="srFrontend"
urlpatterns= [
	url(r'^$', views.index, name='index'),
	url(r'^about.html$', views.about, name='about')
	# url(r'^index.html$', views.index, name='index2')
]