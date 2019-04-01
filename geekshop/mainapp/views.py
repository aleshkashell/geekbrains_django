from django.shortcuts import render

content = {'links_menu': [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'products:index', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'}
    ]}


def main(request):
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)
    return render(request, 'mainapp/catalog.html', content)


def contact(request):
    return render(request, 'mainapp/contacts.html', content)
