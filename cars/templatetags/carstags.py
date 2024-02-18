from django import template
import cars.views as views
from cars.models import Categories

register = template.Library()



@register.inclusion_tag('cars/list_categories.html')
def show_categories():
    cats = Categories.objects.all()
    return {'cats': cats}

