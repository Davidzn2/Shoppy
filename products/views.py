# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import ProductForm
from .models import Product
# Create your views here.

def product_detail(request, pk):
	product = 	get_object_or_404(Product,pk=pk)
	template = loader.get_template('detail.html')
	context={
		'product':product
	}
	return render(request,'detail.html',context)
	class Meta:
		ordering=('id',)

def new_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			product.save
			return HttpResponseRedirect('/')
	else:
		form=ProductForm()
	context= {
		'form':form
	}
	return render(request,'new_product.html', context)


class ProductList(ListView):
	model = Product

class ProductDetail(DetailView):
	model = Product 

