# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from .models import Product
# Create your views here.

def hello_world(request):
	product = Product.objects.order_by('id')
	context = {
		'title': 'Shoppy',
		'product' : product
	}
	return render(request,'index.html',context)

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
		form = ProductForm(request.POST)
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