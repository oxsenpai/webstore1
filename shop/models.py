from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Категория")
    slug = models.SlugField(max_length = 100, unique = True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse('category', kwargs = {'category_slug': self.slug})

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория')
    name = models.CharField(max_length= 100, verbose_name= "Название")
    slug = models.SlugField(max_length= 100)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank= True, verbose_name= "Изображение")
    description = models.TextField(blank= True, verbose_name= 'Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount = models.IntegerField(
        validators= [MinValueValidator(0), MaxValueValidator(100)],
        default= 0,
        verbose_name= "Скидка",
        help_text= "Значение в процентах"
    )
    available = models.BooleanField(default=True,
                                    verbose_name='В продаже')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата добавления')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Дата последнего обновления')

    class Meta:
        ordering = ["name"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def get_absolute_url(self):
        return reverse('product', kwargs = {'product_slug': self.slug})

    def get_discount(self):
        if self.discount:
            return self.discount / Decimal(100) \
                * self.price
        return 0

    def get_price_after_discount(self):
        return Decimal('{:.2f}'.format(self.price - self.get_discount()))

    def __str__(self):
        return self.name



class AdditionalProductImage(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              verbose_name='Изображение')
    product = models.ForeignKey(Product,
                                related_name='additional_images',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'
