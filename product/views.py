from django.shortcuts import render

from .models import Product , Category
from .forms import(CategoryModelform , ProductModelForm) 


def home(request):
    product_list = product.objects.all()
    form = CategoryModelform()
    
    context = {

             'produit_list' : product_list,
             'title' :'Mon titre',
             'number': 55,
             'form' :  form 
    }
    return render(request,"product/index.html ",context)


def add_product(request):
       
    form = ProductModelForm(request.POST or None, request.files or None) 

    if request.method == "POST" :
        form.save()
        form = ProductModelForm()
    else:
        form = ProductModelForm()

    context = {
            'form' : form
    }        
    return render (request, 'product/add_product.html', context)


def edit_product(request,pk):
    product = Product.objects.get(id=pk)
    form = ProductModelForm (request.POST,request.FILES,instance=product)

    if request.method == "POST" :
        form.save()

    context = {
        'form': form

    }    
    return render (request ,'product/edit_product.html',context)
    

def delete_product(request,pk):  
    pass  

def product_list(request):
    products = Product.objects.all()
    context ={
            'product_list' : products 
    }
    return render (request , 'product/product_list.html',context)
    

    
def product_detail(request,id):
    product = product.objects.get(id=id)
    context ={
            'product' : product 
    }
    return render (request , 'product/detail.html',context) 


               

    
   
