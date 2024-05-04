from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.
def home(request):
    
    return render(request,'home.html')

def productadd(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render (request,'productadd.html', {'form':form})

def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html', {'products':products})


def product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'product_view.html', {'product':product})



def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')