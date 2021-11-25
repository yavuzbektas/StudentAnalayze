# Generated by Django 3.2.5 on 2021-11-25 12:19

import apps.polls.views
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211125_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kullanicilar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name=models.CharField(max_length=11, unique=True, validators=[apps.polls.views.validateEven])),
        ),
        migrations.AlterField(
            model_name='raporogrenci',
            name='roporTuru',
            field=models.CharField(choices=[('not', 'Not Raporu'), ('dıs', 'DİS'), ('anket', 'Anket')], max_length=10),
        ),
    ]
