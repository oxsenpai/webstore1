from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "home"),
    path('products/', views.products, name = "products"),
    path('about/', views.about, name = "about"),
    path('faqs/', views.faqs, name = "faqs"),

    path('contact/', views.contact, name = "contact"),
    path('category/<slug:category_slug>/', views.show_category, name = "category"),
    path('product/<slug:product_slug>/', views.show_product, name = "product")
]


