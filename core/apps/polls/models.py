
from django.db import models
from django.utils import timezone
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, IntegerField, TextField
#from .views import validateeven,validateHesCode,validatePhone
# Create your models here.
from  apps.polls.views import validateHesCode, validatePhone , validateEven

class Donem(models.Model):# deneme 
    yillar=models.CharField(max_length=10,default="")
    
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
    
    ad= models.CharField(max_length=20,unique=False)
    soyAd=models.CharField(max_length=20,unique=False)
    TC=models.CharField(max_length=11,unique=True,validators=[validateEven])# regex eklenecek, validasyon yapilacak
    image=models.ImageField(null=True,blank=True,upload_to="images/%Y/")
    gorev=models.ForeignKey(GorevTablosu,on_delete=models.CASCADE,unique=False,related_name="user")
    telefonNo=models.CharField(validators=[validatePhone], max_length=17, blank=True,default="0",null=True,unique=False) # regex eklenecek, validasyon yapilacak
    adres=models.TextField(max_length=75,unique=False)
    calismaDurumu=models.BooleanField(default=True)
    yetki=models.BooleanField(default=False)
    hes_Kodu=models.CharField(max_length=12,unique=True,validators=[validateHesCode])
    dogumTarihi=models.DateField(("Doğum Tarihiniz"), auto_now=False, auto_now_add=False)
    email=models.EmailField()
    CINSIYET=(('KIZ','Kız'),
              ('erkek','Erkek'),
              ('diger','Diğer'),
    )
    cinsiyet=CharField(max_length=10 ,choices=CINSIYET,unique=False) 
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
        if self.image.name !="":
            self.image.name = self.TC+".png"
        
        super(Kullanicilar, self).save(*args, **kwargs)
class OgrenciListesi(models.Model):
    ad= models.CharField(max_length=20,default="",unique=False)
    soyAd=models.CharField(max_length=20,unique=False)
    TC = models.CharField(max_length=11,unique=True,validators=[validateEven])
    telefonNo = models.CharField(validators=[validatePhone], max_length=17, blank=True,default="0",null=True,unique=False)
    adres=models.TextField(unique=False)
    okulDevamDurumu=models.BooleanField(null=False,default=True)
    geldigiOkul=models.ForeignKey(OrtaOkulListesi,on_delete=models.CASCADE)
    kayitYili=models.ForeignKey(Donem,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='images')
    saglikDurumu=models.TextField(unique=False,null=True,)
    hes_Kodu=models.CharField(max_length=12,unique=True,validators=[validateHesCode])
    dogumTarihi=DateField(("Doğum Tarihiniz"), auto_now=False, auto_now_add=False)
    ogrenciNo=models.IntegerField()
    email=models.EmailField()
    CINSIYET=(('KIZ','Kız'),
              ('erkek','Erkek'),
              ('diger','Diğer'),
    )
    cinsiyet=CharField(max_length=10 ,choices=CINSIYET)
    
    
    def __str__(self):
        return self.ad +' '+self.soyAd
    def save(self, *args, **kwargs):
        """ This step is just formatting: add the dash if missing """
        if '-' not in self.hes_Kodu:
            self.hes_Kodu = '{0}-{1}-{2}'.format(
                 self.hes_Kodu[:4], self.hes_Kodu[4:9], self.hes_Kodu[9:])
        if '-' not in self.telefonNo:
            self.telefonNo = '({0})-{1} {2}'.format(
                 self.telefonNo[:4], self.telefonNo[4:7], self.telefonNo[7:])
        
        # Continue the model saving
        super(OgrenciListesi, self).save(*args, **kwargs)
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
    subeAdi=models.ForeignKey(SubeListesi,on_delete=models.CASCADE,default="")
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
    cevaplar=models.ForeignKey(cevaplar,on_delete=models.CASCADE)
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