from .models import Category

def category_of_products(request):
    return {'category_of_products': Category.objects.all()}