from django import template
from AppOrder.models import Order, Cart

register = template.Library()

@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user, ordered=False)

    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0    