from django.contrib import admin

# Register your models here.
from .models import Product, Category, User, Cart, CartItem, Order, Orderitem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
   #  prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # Add customizations for model Category

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    # Add further customizations for User model
    fields = ['username', 'email']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
   

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'total_price')
    list_filter = ('cart', 'product')
    # Add customizations for the CartItem model if needed

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at', 'total_price')
    list_filter = ('user', 'status')

    # further customizations for the Order model

admin.site.register('orderitem')