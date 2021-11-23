# Generated by Django 3.2.6 on 2021-11-22 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20211122_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogrencilistesi',
            name='geldigiOkul',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ortaokullistesi'),
        ),
        migrations.AlterField(
            model_name='raporogrenci',
            name='roporTuru',
            field=models.CharField(choices=[('not', 'Not Raporu'), ('anket', 'Anket'), ('dıs', 'DİS')], max_length=10),
        ),
    ]
