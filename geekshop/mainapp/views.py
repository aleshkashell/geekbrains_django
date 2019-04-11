from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
import random


main_links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'products:index', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'}
    ]


def get_basket_sum(request):
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()
    total = 0
    for product in basket:
        position = get_object_or_404(Product, pk=product.pk)
        total = total + position.price * product.quantity
    return total


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]

    
def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).\
                                    exclude(pk=hot_product.pk)[:3]

    return same_products

def main(request):
    title = 'Главная'
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()
    content = {
            'title': title,
            'links_menu': main_links_menu,
            'basket': basket
        }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'Категории'
    categories = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'Все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        content = {
            'title': title,
            'links_menu': main_links_menu,
            'category': category,
            'products': products,
            'categories': categories,
            'basket': basket
        }
        return render(request, 'mainapp/products.html', content)
    same_products = Product.objects.all()[3:5]
    content = {
        'title': title, 
        'links_menu': main_links_menu, 
        'same_products': same_products,
        'categories': categories,
        'basket': basket
    }
    print(categories)
    return render(request, 'mainapp/catalog.html', content)


def contact(request):
    title = 'Контакты'
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()
    content = {
            'title': title,
            'links_menu': main_links_menu,
            'basket': basket
        }
    return render(request, 'mainapp/contacts.html', content)

def product(request, pk):
    title = 'продукты'
    content = {
        'title': title,
        'links_menu': main_links_menu,
        'product_links_menu': ProductCategory.objects.all(), 
        'product': get_object_or_404(Product, pk=pk), 
        'basket': get_basket(request.user),
    }
    
    return render(request, 'mainapp/product.html', content)
