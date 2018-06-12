from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Tag

class TagListView(ListView):
    queryset = Tag.objects.all()
    context_object_name = "tag_list"
    template_name = "tags/tags.html"



class TagRelatedProductsView(DetailView):
    template_name = "tags/tag_related_products.html"
    context_object_name = "object"
    def get_object(self, queryset=None):
        print("tag value is ",self.kwargs.get("slug"))
        qs=Tag.objects.filter(slug=self.kwargs.get("slug"))
        return qs.first()