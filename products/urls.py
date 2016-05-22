from django.conf.urls import include, url
from . import views
urlpatterns=[
	url(r'^$', views.hello_world, name='hola_mundo'),
	url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail,name='detail'),
	url(r'^product/new',views.new_product, name="new_product"),

]