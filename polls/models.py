from django.db import models
from django.utils import timezone
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from polls.views import validate_even, validate_evenz,validateHesCode

# Create your models here.

class Donem(models.Model):
    yillar=models.TextField(max_length=10,default="")
    
    def __str__(self): 
      return self.yillar
   
 
     

class Question(models.Model):
    question_text = models.CharField(max_length=200,default="")
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,default="")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
  


class OrtaOkulListesi(models.Model):
    okulAdi=models.CharField(max_length=100,default="")
    def __str__(self): 
        return self.okulAdi
class SoruListesi(models.Model):
    sorular=models.CharField(max_length=200,default="")
    def __str__(self): 
        return self.sorular


class GorevTablosu(models.Model):
    brans=models.TextField(max_length=30,default="")
    def __str__(self): 
        return self.brans


class Kullanicilar(models.Model):
    
    ad= models.CharField(max_length=20)
    soyAd=models.CharField(max_length=20)
    TC=models.IntegerField(unique=True,validators=[validate_even],max_length=17,)# regex eklenecek, validasyon yapilacak
    
    image=models.ImageField(null=True,blank=True,upload_to='images',verbose_name=TC)
    gorev=models.ForeignKey(GorevTablosu,on_delete=models.CASCADE)
    telefonNo=models.CharField(validators=[validate_evenz], max_length=17, blank=True,default="0",null=True) # regex eklenecek, validasyon yapilacak
    adres=TextField(max_length=75)
    calismaDurumu=models.BooleanField()
    yetki=models.BooleanField()
    hes_Kodu=models.CharField(max_length=12,unique=True,validators=[validateHesCode])
    dogumTarihi=DateField(("Doğum Tarihiniz"), auto_now=False, auto_now_add=False)
    email=models.EmailField()
    CINSIYET=(('KIZ','Kız'),
              ('erkek','Erkek'),
              ('diger','Diğer'),
    )
    cinsiyet=CharField(max_length=10 ,choices=CINSIYET) 
    def __str__(self):
        return self.ad +' '+ self.soyAd
    def save(self, *args, **kwargs):
        """ This step is just formatting: add the dash if missing """
        if '-' not in self.hes_Kodu:
            self.hes_Kodu = '{0}-{1}-{2}'.format(
                 self.hes_Kodu[:4], self.hes_Kodu[4:9], self.hes_Kodu[9:])
        if '-' not in self.telefonNo:
            self.telefonNo = '({0})-{1} {2}'.format(
                 self.telefonNo[:4], self.telefonNo[4:7], self.telefonNo[7:])
        # Continue the model saving
        super(Kullanicilar, self).save(*args, **kwargs)
    
  
class OgrenciListesi(models.Model):
    ad= models.CharField(max_length=20,default="",editable=False)
    soyAd=models.CharField(max_length=20)
    TC = models.IntegerField(validators=[validate_even])
    
    telefonNo=models.IntegerField(unique=True,validators=[validate_evenz])
    adres=models.TextField()
    okulDevamDurumu=models.BooleanField(null=False)
    geldigiOkul=models.OneToOneField(OrtaOkulListesi,on_delete=models.CASCADE)
    kayitYili=models.OneToOneField(Donem,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='images')
    saglikDurumu=models.TextField()
    hesKodu=models.CharField(max_length=12,unique=True)
    dogumTarihi=models.CharField(max_length=12)
    ogrenciNo=models.IntegerField()
    email=models.EmailField()
    CINSIYET=(('KIZ','Kız'),
              ('erkek','Erkek'),
              ('diger','Diğer'),
    )
    cinsiyet=CharField(max_length=10 ,choices=CINSIYET)
    
    
    def __str__(self):
        return self.ad +' '+self.soyAd
    
class VeliListesi(models.Model):
    ad= models.CharField(max_length=20,default="")
    soyAd=models.CharField(max_length=20)
    ogrenci=models.ManyToManyField(OgrenciListesi)
    yakinlikDurumu=models.CharField(max_length=20)
    telefonNo=models.IntegerField()
    adres=models.TextField()
    meslek=models.CharField(max_length=20)

    def __str__(self):
        return self.ad
class SubeListesi(models.Model):
    subeAdi=models.CharField(default="A",max_length=1,unique=True)
    def __str__(self): 
        return self.subeAdi
class SinifListesi(models.Model):
    ogrrenciListesi=models.ForeignKey(OgrenciListesi,models.CASCADE)
    subeAdi=models.OneToOneField(SubeListesi,on_delete=models.CASCADE,default="")
    donem=models.ForeignKey(Donem,on_delete=models.CASCADE)
    SECENEKLER=(
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),

    )
    sinifNo=models.CharField(max_length=2,choices=SECENEKLER)
    
       

    def __str__(self):
        
        return str(self.donem.yillar)+' '+str(self.sinifNo)+self.subeAdi.subeAdi
class DersIzlemeSinavlari(models.Model):
    disVerileri=models.TextField(default="")
class AnketListesi(models.Model):
    sorular=models.ForeignKey(SoruListesi,on_delete=models.CASCADE,default="")
    donem=models.ForeignKey(Donem,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.donem.yillar)+' Anketi'
    
class cevaplar(models.Model):
    cevap=models.TextField()
class RaporOgrenci(models.Model):
    RAPOR={
        ('dıs','DİS'),
        ('anket','Anket'),
        ('not','Not Raporu'),

    }
    roporTuru=models.CharField(max_length=10,choices=RAPOR)
    anket_sonucu=models.ForeignKey(AnketListesi,on_delete=models.CASCADE)
    degerlendiren=models.ForeignKey(Kullanicilar,on_delete=models.CASCADE)
    cevaplar=models.OneToOneField(cevaplar,on_delete=models.CASCADE)
    donem=models.ForeignKey(Donem,on_delete=models.CASCADE)
    ogrenci=models.ForeignKey(OgrenciListesi,on_delete=models.CASCADE)
    def __str__(self) :
        return str(self.donem.yillar)+' '+'Öğrenci Raporu'
class RaporSinif(models.Model):
    dis=models.ForeignKey(DersIzlemeSinavlari,on_delete=models.CASCADE,default="")
    anket_sonucu=models.ForeignKey(AnketListesi,on_delete=models.CASCADE)
    sinif=models.ForeignKey(SinifListesi,on_delete=models.CASCADE)
    def __str__(self) :
        return str(self.sinif.sinifNo)+self.sin