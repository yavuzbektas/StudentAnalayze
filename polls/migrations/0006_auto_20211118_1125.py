# Generated by Django 3.2.5 on 2021-11-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_donem_yıllar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dersizlemesinavlari',
            old_name='dis_verileri',
            new_name='disVerileri',
        ),
        migrations.RenameField(
            model_name='donem',
            old_name='yıllar',
            new_name='yillar',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='last_name',
            new_name='ad',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='adress',
            new_name='adres',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='Çalışma_Durumu',
            new_name='calismaDurumu',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='name',
            new_name='soyAd',
        ),
        migrations.RenameField(
            model_name='kullanicilar',
            old_name='phoneNumber',
            new_name='telefonNo',
        ),
        migrations.RenameField(
            model_name='ogrencilistesi',
            old_name='last_name',
            new_name='ad',
        ),
        migrations.RenameField(
            model_name='ogrencilistesi',
            old_name='adress',
            new_name='adres',
        ),
        migrations.RenameField(
            model_name='ogrencilistesi',
            old_name='KayıtYılı',
            new_name='kayitYili',
        ),
        migrations.RenameField(
            model_name='ogrencilistesi',
            old_name='OkulDevam',
            new_name='okulDevamDurumu',
        ),
        migrations.RenameField(
            model_name='ogrencilistesi',
            old_name='name',
            new_name='soyAd',
        ),
        migrations.RenameField(
            model_name='ortaokullistesi',
            old_name='name',
            new_name='okulAdi',
        ),
        migrations.RenameField(
            model_name='raporsinif',
            old_name='sınıf',
            new_name='sinif',
        ),
        migrations.RenameField(
            model_name='siniflistesi',
            old_name='sınıf_no',
            new_name='sinifNo',
        ),
        migrations.RenameField(
            model_name='siniflistesi',
            old_name='sube_adi',
            new_name='subeAdi',
        ),
        migrations.RenameField(
            model_name='subelistesi',
            old_name='name',
            new_name='subeAdi',
        ),
        migrations.RenameField(
            model_name='velilistesi',
            old_name='last_name',
            new_name='ad',
        ),
        migrations.RenameField(
            model_name='velilistesi',
            old_name='Yakınlık_Durumu',
            new_name='adres',
        ),
        migrations.RenameField(
            model_name='velilistesi',
            old_name='name',
            new_name='soyAd',
        ),
        migrations.RenameField(
            model_name='velilistesi',
            old_name='phoneNumber',
            new_name='telefonNo',
        ),
        migrations.RenameField(
            model_name='velilistesi',
            old_name='adress',
            new_name='yakinlikDurumu',
        ),
        migrations.AddField(
            model_name='ogrencilistesi',
            name='telefonNo',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
