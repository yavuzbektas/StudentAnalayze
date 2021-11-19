from django.db import models
from django.utils import timezone
from django.db.models.aggregates import Max
from django.db.models.deletion import CASCADE

from django.db.models.fields import IntegerField
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class OrtaOkulListesi(models.Model):
    okulAdi=models.CharField(max_length=100)
    def __str__(self): 
        return self.okulAdi
class SoruListesi(models.Model):
    sorular=models.TextField()
    def __str__(self): 
        return self.sorular
class Donem(models.Model):
    yillar=models.TextField(max_length=15)
    def __str__(self): 
        return self.yillar

class GorevTablosu(models.Model):
    brans=models.CharField(max_length=20)
    def __str__(self): 
        return self.brans


class Kullanicilar(models.Model):
    ad= models.CharField(max_length=20)
    soyAd=models.CharField(max_length=20)
    TC=models.IntegerField(max_length=11,unique=True)# regex eklenecek, validasyon yapilacak
    gorev=models.ManyToManyField(GorevTablosu)
    telefonNo=models.IntegerField(max_length=10) # regex eklenecek, validasyon yapilacak
    adres=models.TextField()
    calismaDurumu=models.BooleanField()
    yetki=models.BooleanField()
    def __str__(self):
        return "K:{} {}  - {}".format(self.ad,self.soyAd,self.gorev,)
    

class OgrenciListesi(models.Model):
    ad= models.CharField(max_length=20)
    soyAd=models.CharField(max_length=20)
    TC=models.IntegerField(max_length=11,unique=True)
    telefonNo=models.IntegerField(max_length=10)
    adres=models.TextField()
    okulDevamDurumu=models.BooleanField(null=False)
    geldigiOkul=models.OneToOneField(OrtaOkulListesi,on_delete=models.CASCADE)
    kayitYili=models.OneToOneField(Donem,on_delete=models.CASCADE)
    
    
class VeliListesi(models.Model):
    ad= models.CharField(max_length=20)
    soyAd=models.CharField(max_length=20)
    ogrenci=models.ManyToManyField(OgrenciListesi)
    yakinlikDurumu=models.CharField(max_length=20)
    telefonNo=models.IntegerField(max_length=10)
    adres=models.TextField()
    meslek=models.CharField(max_length=20)
    
class SubeListesi(models.Model):
    subeAdi=models.CharField(max_length=1,default= "A",unique=True)
    def __str__(self): 
        return self.subeAdi
class SinifListesi(models.Model):
    ogrenci=models.ForeignKey(OgrenciListesi,on_delete=models.CASCADE)
    subeAdi=models.OneToOneField(SubeListesi,on_delete=models.CASCADE)
    donem=models.OneToOneField(Donem,on_delete=models.CASCADE)
    sinifNo=models.IntegerField()
class DersIzlemeSinavlari(models.Model):
    disVerileri=models.TextField()
class AnketListesi(models.Model):
    sorular=models.ForeignKey(SoruListesi,on_delete=models.CASCADE)
class RaporOgrenci(models.Model):
    dis=models.ForeignKey(DersIzlemeSinavlari,on_delete=models.CASCADE)
    anket_sonucu=models.ForeignKey(AnketListesi,on_delete=models.CASCADE)
    degerlendiren=models.ManyToManyField(Kullanicilar)
    cevaplar=models.IntegerField()
    donem=models.OneToOneField(Donem,on_delete=models.CASCADE)

class RaporSinif(models.Model):
    dis=models.ForeignKey(DersIzlemeSinavlari,on_delete=models.CASCADE)
    anket_sonucu=models.ForeignKey(AnketListesi,on_delete=models.CASCADE)
    sinif=models.ForeignKey(SinifListesi,on_delete=models.CASCADE)