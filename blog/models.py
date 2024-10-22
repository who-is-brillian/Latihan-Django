from django.db import models

# Create your models here.
class Kategori(models.Model):
    kode = models.CharField(max_length=10)
    nama = models.CharField(max_length=225)
    def __str__(self):
        return"%d. %s" %(self.id, self.nama)

class Article(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    gambar = models.ImageField(upload_to='images/')  # Menyimpan gambar di folder 'images/'
    pilih_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    def __str__(self):
        return "%d. %s" %(self.id, self.judul) 