from django.shortcuts import render, redirect
import requests
from .forms import LocationAddForm


# Create your views here.
def all_locations(request):
    temp = requests.get('http://localhost:8000/locations/api/locs_data', headers={"Authorization" : "Token b2d67b220f7bb3a92c82e300e32e1fdd206443af"})
    print(temp)
    return render(request, 'locations/all_locations.html', {'data':temp.json()})
def add_locations(request):
    form = LocationAddForm
    if request.method == 'POST':
        form = LocationAddForm(request.POST)
        if form.is_valid():
            product_data = {"bno": form.cleaned_data['bno'],
                "street": form.cleaned_data['street'],
                "area": form.cleaned_data['area'],
                "state": form.cleaned_data['state'],
                }
            temp = requests.post('http://localhost:8000/locations/api/locs_data', headers={"Authorization" : "Token b2d67b220f7bb3a92c82e300e32e1fdd206443af"}, data=product_data)
            return redirect('all_locations')
    return render(request, 'locations/add_locations.html', {'form':form})

