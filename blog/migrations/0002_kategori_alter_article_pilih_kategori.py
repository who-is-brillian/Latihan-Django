# Generated by Django 5.1.1 on 2024-10-22 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=225)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='pilih_kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.kategori'),
        ),
    ]