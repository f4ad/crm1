from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.EmailField()
    date_create=models.DateTimeField(auto_now_add=True)
    #To show customer name on admin panel.
    def __str__(self):
        return self.name


class tag(models.Model):
    name=models.CharField(max_length=200)

    #To show customer name on admin panel.
    def __str__(self):
        return self.name
class products(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
    )
    name=models.CharField(max_length=200)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,choices=CATEGORY)
    description=models.CharField(max_length=200, null=True,blank=True)
    date_create=models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tag)
    def __str__(self):
        return self.name

class order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(Customer,null= True, on_delete=models.SET_NULL)
    products=models.ForeignKey(products,null=True, on_delete=models.SET_NULL)
    date_create=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.products.name




