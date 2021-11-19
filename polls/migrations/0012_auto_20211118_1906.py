# Generated by Django 3.2.5 on 2021-11-18 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20211118_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gorevtablosu',
            name='brans',
            field=models.CharField(max_length=20),
        ),
        migrations.RemoveField(
            model_name='kullanicilar',
            name='gorev',
        ),
        migrations.AddField(
            model_name='kullanicilar',
            name='gorev',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.gorevtablosu'),
            preserve_default=False,
        ),
    ]
