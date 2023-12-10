from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.core.paginator import Paginator

from .models import Category, Product



def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {'products': products, 'page_obj': page_obj}

    return render(request, 'shop/index.html', context=data)

def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    data = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'shop/products.html', context=data)

def show_category(request, category_slug):


    category = get_object_or_404(Category, slug = category_slug )
    cat_id = category.id
    products = Product.objects.filter(category=cat_id)
    data = {
        'category': category,
        'products': products

    }

    return render(request, 'shop/category.html', context=data)

def show_product(request, product_slug):
    product = get_object_or_404(Product, slug = product_slug)
    products = Product.objects.filter(category = product.category)[:4]
    data = {
        'product': product,
        'products': products
    }

    return render(request, 'shop/product.html', context=data)

def about(request):
    return render(request, 'shop/about.html')

def faqs(request):
    return render(request, 'shop/faqs.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def contact(request):
    return render(request, 'shop/contact.html')

def page_not_found(request, exception):
    return HttpResponseNotFound('404')
