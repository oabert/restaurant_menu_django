from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_CATEGORY


class MenuList(generic.ListView):
    queryset = Item.objects.order_by('-date_created')  # if add '-' receive reverse order
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        # contex = {'meals':MEAL_CATEGORY}
        contex['meals'] = MEAL_CATEGORY
        return contex


class MenuItemDetails(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'
