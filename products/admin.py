from django.contrib import admin
from .models import Product, Favorite


# admin.site.register(Product)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
	list_display = ('id','name','category','description','price')
	list_filter = ('id','name','category')
@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
	list_display=('user','product',)
	list_filter=('user','product',)