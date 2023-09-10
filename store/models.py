from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Category(models.Model):
    """class model for category
    """
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """string representation
        """
        return self.name

class Product(models.Model):
    """ class model for product"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/' null=True, blank=True)
    
    def __str__(self):
        """ string represention"""
        return self.name


class Customer(AbstractUser):
    """ class model for customer """
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    
    def __str__(self):
        """ string representation """
        return self.username

class Order(models.Model):
    """ class model for Order """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        """ string repersentation"""
        return ('Order #{} by {}'.format(self.id, self.customer.username))
    

class OrderItem(models.Model):
    """ class model for order items"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PostiveIntegerField()
    item_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        """string represenation """
        return ('{} X {}'.format(self.quantity, self.product.name))
    
    def save(self, *args, **kwargs):
        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)


class Payment(models.Model):
    """ class model for payment """
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        """ string representation"""
        return ("payment for Order #{}".format(self.order.id))
    