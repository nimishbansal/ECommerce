from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
# Create your views here.
from .models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_details.html"


    def get_object(self, queryset=None):
        print("looking pk ",self.kwargs)
        instance=Product.objects.get_by_id(self.kwargs.get("pk"))
        if (instance==None):
            raise Http404("Product does not exist")
        return instance

        # print("looking pk ",self.kwargs)
        # return get_object_or_404(Product,id=self.kwargs.get("pk"))


class ProductListView(ListView):
    template_name = "products/product_list.html"
    queryset = Product.objects.all()
    context_object_name = "products_list"



class ProductFeaturedDetailView(DetailView):
    model = Product
    template_name = "products/featured_product_detail.html"

    def get_object(self, queryset=None):
        slug = self.kwargs.get("slug")
        print(slug)
        instance = get_object_or_404(Product, slug=slug)
        if instance is None:
            raise Http404("Product not exist hehe")
        return instance


class ProductFeaturedListView(ListView):
    template_name = "products/featured_product_list.html"
    queryset = Product.objects.featured()
    context_object_name = "products_list"


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name="products/product_details.html"

    def get_object(self, queryset=None):
        slug=self.kwargs.get("slug")
        print(slug)
        instance=get_object_or_404(Product,slug=slug)
        if instance is None:
            raise Http404("Product not exist hehe")
        return instance



class ProductSearchView(ListView):
    template_name = "products/product_list.html"
    queryset = Product.objects.all()
    context_object_name = "products_list"


    def get(self, request, *args, **kwargs):
        ans=super(ProductSearchView,self).get(request,*args,**kwargs)
        print(ans)
        return ans