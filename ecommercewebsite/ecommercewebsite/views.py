from django.shortcuts import render

from .forms import ContactForm


def home_page(request):
    return render(request,"home_page.html")


def contact_page(request):
    contact_form=ContactForm()
    print(request.POST)
    return render(request,"contactus_page.html",{"form":contact_form})

