from django.shortcuts import render, redirect
import requests
from .forms import ProductAddForm, OriginForm


# Create your views here.
def all_products(request):
    temp = requests.get('http://localhost:8000/api/productsdata', headers={"Authorization" : "Token b2d67b220f7bb3a92c82e300e32e1fdd206443af"})
    return render(request, 'products/all_products.html', {'data':temp.json()})

def add_products(request):
    form = ProductAddForm
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            product_data = {"product_name": form.cleaned_data['product_name'],
                "mrp": form.cleaned_data['mrp'],
                "discount": form.cleaned_data['discount'],
                "price": form.cleaned_data['price'],
                "quantity": form.cleaned_data['quantity'],
                "origin": form.cleaned_data['origin'],
                "description": form.cleaned_data['description'],
                }
            temp = requests.post('http://localhost:8000/api/productsdata', headers={"Authorization" : "Token b2d67b220f7bb3a92c82e300e32e1fdd206443af"}, data=product_data)
            return redirect('all_products')
    return render(request, 'products/add_products.html', {'form':form})

def get_origin(request):
    temp = {}
    form = OriginForm
    if request.method == 'POST':
        form = OriginForm(request.POST)
        if form.is_valid():
            place = form.cleaned_data['place']
            temp = requests.get('http://localhost:8000/api/origin_data/' + place, headers={"Authorization" : "Token b2d67b220f7bb3a92c82e300e32e1fdd206443af"})
            return render(request, 'products/origin.html', {'form':form, 'data':temp.json()})

    return render(request, 'products/origin.html', {'form':form})


