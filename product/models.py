from django.db import models


class Category(models.Model):

    '''model to store category for the product.'''

    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name 


class Product(models.Model):

    ''' models to store product details.'''
    name = models.CharField(max_length=50,null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    is_added = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    
    '''models to store tag for the products'''

    tag_name = models.CharField(max_length=50)
    product = models.ManyToManyField(Product)
    def __str__(self):
        return self.tag_name