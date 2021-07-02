from django.shortcuts import render
from django.views.generic import ListView

from core.erp.models import Product


class ProductsListView(ListView):
    model = Product
    template_name = ''
    def __str__(self):
        return self.name

    class Meta:
        pass
