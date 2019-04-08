from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404


main_links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'products:index', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'}
    ]


def main(request):
    title = 'Главная'
    content = {
            'title': title,
            'links_menu': main_links_menu
        }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'Категории'
    categories = ProductCategory.objects.all()
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
            'categories': categories
        }
        return render(request, 'mainapp/products.html', content)
    same_products = Product.objects.all()[3:5]
    content = {
        'title': title, 
        'links_menu': main_links_menu, 
        'same_products': same_products,
        'categories': categories
    }
    print(categories)
    return render(request, 'mainapp/catalog.html', content)


def contact(request):
    title = 'Контакты'
    content = {
            'title': title,
            'links_menu': main_links_menu
        }
    return render(request, 'mainapp/contacts.html', content)
