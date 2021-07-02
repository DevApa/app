from django.shortcuts import render
from django.views.generic import ListView


class ProductsListView(ListView):
    model = Products
    def __str__(self):
        return self.name

    class Meta:
        pass
