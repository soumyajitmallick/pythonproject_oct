from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def product_list(request, product_id=None):
    products=Product.objects.all()
    form=ProductForm()

    if product_id:
        product=get_object_or_404(Product,pk=product_id)
        form=ProductForm(isinstance=product)
    
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()  # Reset the form after saving
    
    return render(request, 'product_list.html', {'products':products, 'form':form})


def edit_or_delete_product(request, product_id):
    products=Product.objects.all()
    product=get_object_or_404(Product, pk=product_id)

    if request.method=='POST':
        form=ProductForm(request.POST, instance=product)
        print(request.POST)
        if 'edit' in request.POST :  # and form.is_valid():
            form=ProductForm(instance=product)
            return render(request, 'product_list.html',  {'products':products,'product':product, 'form':form})

        elif 'delete' in request.POST:
            product.delete()

        else :
            product . name = request . POST ['name']
            product . description = request . POST ['description']
            product . price = request . POST ['price']
            product . save ()
    
    return redirect('product_list')