from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name =  models.CharField(max_length=50, unique=True, verbose_name='Имя категории')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True,verbose_name='Описание')
    car_image = models.ImageField(upload_to='category/%Y/%m/%d/', blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_url(self):
        return reverse('category', args=[self.slug])

    def __str__(self):
        return  self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True, verbose_name='Имя категории')
    slug = models.SlugField(max_length=200, unique=True,)
    description = models.TextField(verbose_name='Описание', blank=True,)
    price = models.IntegerField(verbose_name='Цина')
    price_old = models.IntegerField(default=0, verbose_name='Цена старая', blank=True)
    image = models.ImageField(upload_to='photos/products/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    stock = models.IntegerField(default=0, verbose_name='склад')
    is_available = models.BooleanField(default=True, verbose_name='Опубликовать')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Выбор категории')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])



    def __str__(self):
        return self.product_name

variation_category_choice =(
    ('color', 'color'),
    ('size', 'size'),
)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100,)
    is_active = models.BooleanField(default=True,)
    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.product

    class Meta:
        verbose_name = 'Вариация'
        verbose_name_plural = 'Вариацию'
