# Generated by Django 4.0 on 2021-12-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20211217_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonperiods',
            name='lessName',
            field=models.CharField(default='1.Ders', max_length=15, verbose_name='Ders No'),
        ),
    ]
