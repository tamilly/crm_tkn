from django.db import models

# Create your models here.

#Customers Definition ------------------------------------
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#TAG (relationship many to many) Definition ------------------------------------

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

#Products Definition ------------------------------------

class Product(models.Model):
    CATEGORY = (
        ('Furniture&Decoration', 'Furniture&Decoration'),
        ('Beauty&Fashion', 'Beauty&Fashion'),
        ('Appliances&Split', 'Appliances&Split'),
        ('Imported&Utilities', 'Imported&Utilities'),
        ('Games,Movies&Books', 'Games,Movies&Books'),
        ('Fitness&Health', 'Fitness&Health'),
        ('Innovations', 'Innovations'),
        ('Others', 'Others'),
    )

    name = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

#Order (Relationship one-to-many) Definition ------------------------------------

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    note = models.CharField(max_length=1000, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name
