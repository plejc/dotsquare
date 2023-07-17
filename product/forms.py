from .models import Category, Tag, Product
from django.forms import forms,ModelForm



class CategoryForm(ModelForm):

    ''' forms to create category '''
    class Meta:
        model = Category
        fields = ['name']

class TagForm(ModelForm):

    ''' forms to create tags for the products'''
    class Meta:
        model = Tag
        fields = ['tag_name','product']

class ProductForm(ModelForm):

    '''form to create product for the application.'''
    class Meta:
        model = Product

        fields = ['name','image','price','stock','category']