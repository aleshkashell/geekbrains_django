from django import template

register = template.Library()

@register.filter
def basket_total_cost(user):
    if user.is_anonymous:
        return 0
    else:
        return user.basket.all()[0].total_cost