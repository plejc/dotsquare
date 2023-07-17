from django.shortcuts import render,redirect
from .models import Category,Tag,Product
from .forms import CategoryForm,ProductForm,TagForm
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

def category_list(request):
    '''add category in the tag tables.'''

    context = {}
    context['category'] = Category.objects.all()
    return render(request,'category_list.html', context)

def home(request):
    ''' home view ==='''
    return render(request,'index.html')

def addCategory(request):
    '''logic to add category for the products'''
    if request.method =='POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            # return HttpResponse('created successfully')
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form':form})

def tag_list(request):
    '''tag list view'''

    return render(request,'tag_list.html')

def add_tag(request):
    '''add tag for the products'''
    if request.method =='POst':
        pass

def add_product(request):
    '''logic to add product'''
    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse('created successfully')
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form':form})

def product_list(request):
    '''logic to get list of product added '''
    context = {}
    context['products'] = Product.objects.all()
    return render(request,'product_list.html', context)

def tag_list(request):
    '''logic to get list of all tags'''
    context = {}                
    context['tags'] = Tag.objects.all()
    return render(request,'tag_list.html', context)
def add_tag(request):
    '''logic to create tag for the products'''
    if request.method =='POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Tag created successfully")
            return redirect("tag_list")

    else:
        form = TagForm()
    return render(request,'add_tag.html',{'form':form})
    
#add to cart
def add_to_cart(request,product_id):
    '''logic to add product into cart'''
    product = get_object_or_404(Product,pk=product_id)
    print("the coming product is the following ====", product.id)
    product.is_added = True
    product.save()
    return redirect("product_list")
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    def get_context_data(self, *args, **kwargs):
        print("this is hitting here =====", self.kwargs['pk'])
        context = super(ProductDetailView,
             self).get_context_data(*args, **kwargs)       
        return context
    

#cart list
def cart_list(request):
    '''logic to get all added product list in cart  '''
    context = {}
    context['products'] = Product.objects.filter(is_added=True)
    return render(request,'cart_list.html', context)
