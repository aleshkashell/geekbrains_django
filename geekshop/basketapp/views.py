from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product
import json

main_links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'products:index', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'}
    ]


def get_basket_sum(request):
    basket = request.user.basket.all()
    total = 0
    for product in basket:
        position = get_object_or_404(Product, pk=product.pk)
        total = total + position.price * product.quantity
    return total


def basket(request):
    title = 'Корзина'
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
    content = {
        'title': title,
        'basket_items': basket_items,
        'links_menu': main_links_menu,
    }
    return render(request, 'basketapp/basket.html', content)



def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
