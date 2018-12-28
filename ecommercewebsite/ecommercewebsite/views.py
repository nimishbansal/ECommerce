import math

from django.shortcuts import render

from .forms import ContactForm
from tags.models import Tag

def home_page(request):
    carousel_images=[
        "https://images-eu.ssl-images-amazon.com/images/G/31/img18/Wireless/CEEX/RM1/CITI/updated/Realme1_superhero_1500x300._CB476629090_.jpg",
        "https://images-eu.ssl-images-amazon.com/images/G/31/IN-hq/2018/img/Video_Games-Internet/XCM_Manual_1111900_DIS_PONR-Apr_1500x300_Video-Games-Internet_1111900_1500X300_jpg._CB496237524_.jpg",
        "https://m.media-amazon.com/images/G/31/img18/PC/All-acc/1121574EVERYTHING-computer1500X300._CB476964739_.jpg",
    ]

    tags=Tag.objects.all()

    # tags_tagged_all=[math.ceil(len(tag.tagged.all())/4) for tag in tags]
    context={
        "carousel_images":carousel_images,
        "tags":tags,
        # "tags_tagged_all":tags_tagged_all
    }

    return render(request,"home_page.html",context)


def contact_page(request):
    contact_form=ContactForm()
    print(request.POST)
    return render(request,"contactus_page.html",{"form":contact_form})

