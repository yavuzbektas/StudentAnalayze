# Generated by Django 3.2.5 on 2021-11-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20211118_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kullanicilar',
            name='gorev',
        ),
        migrations.AddField(
            model_name='kullanicilar',
            name='gorev',
            field=models.ManyToManyField(to='polls.GorevTablosu'),
        ),
    ]