from django.contrib import admin

# Register your models here.
from .models import Article, Kategori

admin.site.register(Article)
admin.site.register(Kategori)