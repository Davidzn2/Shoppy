from django.conf.urls import include, url
from . import views
urlpatterns=[
	url(r'^$', views.ProductList.as_view(), name='hola_mundo'),
	url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(),name='detail'),
	url(r'^product/new',views.new_product, name="new_product"),

]