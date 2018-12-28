"""ecommercewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include

from . import views

from carts.views import add_to_cart

urlpatterns = [
    re_path('^$', views.ProductListView.as_view()),
    re_path(r'^search/$', views.ProductSearchView.as_view(),name="search"),

    re_path(r'^featured/$', views.ProductFeaturedListView.as_view()),
    re_path(r'^featured/(?P<slug>[\w-]+)/$', views.ProductFeaturedDetailView.as_view()),

    # re_path(r'(?P<pk>\d+)/$',views.ProductDetailView.as_view(),name="detail"),
    url(r'(?P<slug>[\w-]+)/add_to_cart/$',add_to_cart,name="AddToCart"),
    re_path(r'(?P<slug>[\w-]+)/$',views.ProductDetailSlugView.as_view(),name="detail"),

]
