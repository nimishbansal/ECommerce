from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
# Create your views here.
from .models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_details.html"


    def get_object(self, queryset=None):
        print("looking pk ",self.kwargs)
        return get_object_or_404(Product,id=self.kwargs.get("pk"))

    # def get_context_data(self, **kwargs):
    #     print("hello")
    #     context = super(ProductDetailView, self).get_context_data(**kwargs)
    #     context['object'] = Product.objects.filter(pk=self.kwargs.get("pk"))
    #     return context


