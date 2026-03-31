from django.shortcuts import render, get_object_or_404
from .models import Phone


def catalog(request):
    sort = request.GET.get('sort', 'name')  

    if sort == 'price_asc':
        phones = Phone.objects.order_by('price')
    elif sort == 'price_desc':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.order_by(sort)

    return render(request, 'catalog.html', {'phones': phones})


def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})
