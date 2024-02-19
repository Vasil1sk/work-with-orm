from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort == 'name':
        phones = Phone.objects.order_by('name')
    else:
        phones = Phone.objects.all()
    return render(request, template, {'phones': phones})


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    return render(request, template, {'phone': phone})
