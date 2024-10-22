from django.shortcuts import render
from django.templatetags.static import static  # Import static


def index(request):
    context = {
        'title': 'Home',
        'headline' : 'Welcome to Hole Page',
        "banner1": static('images/Carousel1.png'),
        "banner2": static('images/Carousel2.png'),
        "banner3": static('images/Carousel1.png'),
        }
    return render (request,'index.html', context)