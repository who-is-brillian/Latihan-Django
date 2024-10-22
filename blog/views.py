from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # queryset 
    allArticle = Article.objects.all()
    print(allArticle)
    context = {
        'title' : 'Blog Helu',
        'headline' : 'Halaman Blog',
        'semuaArtikel':allArticle
    }
    return render(request, 'blog.html', context)