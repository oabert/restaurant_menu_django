from django.shortcuts import render
from django.views import generic
from models import Item


class MenuList(generic.ListView):
    queryset = Item.object.order_by('-date_created')  # if add '-' receive reverse order
    template_name = 'index.html'


class MenuItemDetails(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'
