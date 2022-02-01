# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present RoboBusters
"""

from django.core.validators import RegexValidator,ValidationError
from django.db import models
from django.utils import timezone
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from django.contrib.auth.models import User
from django.core.files.base import ContentFile

def validateHesCode(value):
    HesCodeRegex = RegexValidator(regex=r'^[0-9]{4}-?[0-9]{5}$', message="HES Code  must be entered in the format: 'Txxx-xxxx-x'. Up to 9  char allowed.")
def validatePhone(value):
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    
    # y=str(value)
    # x=list(y)    
        
    # if len(x) != 10 :
    #     raise ValidationError(
    #         _('%(value)s 10 basasmaklı olmalı'),
    #         params={'value': value},
    #     )
def validateEven(value):
    y=str(value)
    x=list(y)
        
        
    if len(x) != 11:
        raise ValidationError(
            ('%(value)s 11 basasmaklı olmalı'),
            params={'value': value},
        )
class JobsTable(models.Model):
    name=models.CharField(max_length=50,default="",)
    def __str__(self): 
        return self.name

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(instance.TC), ext)
    print(filename)
    return os.path.join('images/ogretmenler/', filename)    

class Profil(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
    TC=models.CharField(max_length=11,unique=True,validators=[validateEven],blank=True,null=True)# regex eklenecek, validasyon yapilacak
    image=models.ImageField(upload_to=upload_location,blank=True,null=True,default='images/person.png')
    job=models.ForeignKey(JobsTable,on_delete=models.CASCADE,unique=False,blank=True,null=True)
    phone=models.CharField(validators=[validatePhone], max_length=17, blank=True,default="05",null=True,unique=False) # regex eklenecek, validasyon yapilacak
    adress=models.TextField(max_length=100,unique=False,blank=True,null=True)
    isWorking=models.BooleanField(default=True,unique=False,blank=True,null=True)
    HESCode=models.CharField(max_length=12,unique=True,validators=[validateHesCode],blank=True,null=True)
    birthdate=models.DateField(("Doğum Tarihiniz"), auto_now=False, auto_now_add=False,unique=False,blank=True,null=True)
    sexualChoice=(('Kız','Kız'),
              ('Erkek','Erkek'),
              ('Diger','Diğer'),
    )
    gender=CharField(max_length=10 ,choices=sexualChoice,unique=False,blank=True,null=True) 
    
    
    def __str__(self):
        if self.TC!=None and self.user.first_name!=None  and self.user.last_name!=None :
            return self.TC + " - "+self.user.first_name+ " "+ self.user.last_name
        else :
            return "profil bos"
    def save(self, *args, **kwargs):
        """ This step is just formatting: add the dash if missing """
        if self.HESCode!=None:
            if '-' not in self.HESCode :
                self.HESCode = '{0}-{1}-{2}'.format(
                 self.HESCode[:4], self.HESCode[4:9], self.HESCode[9:])
        if self.phone!=None:       
            if '-' not in self.phone:
                self.phone = '({0})-{1} {2}'.format(
                 self.phone[:4], self.phone[4:7], self.phone[7:])
        # Continue the model saving
        #https://stackoverflow.com/questions/15140942/django-imagefield-change-file-name-on-upload
        
        
        super(Profil, self).save(*args, **kwargs)
class Session(models.Model):
    session=models.CharField(max_length=10,default="2021-2022",unique=True)
    active=models.BooleanField(default=False)
    def __str__(self): 
      return self.session
class Period(models.Model):
    period=models.CharField(max_length=10,default="1.Dönem",unique=True)
    active=models.BooleanField(default=False)
    def __str__(self):
      return self.period
class SessionPeriod(models.Model):
    session=models.ForeignKey(Session,on_delete=models.CASCADE)
    period=models.ForeignKey(Period,on_delete=models.CASCADE)
    def __str__(self): 
      return self.session.session + "-" + self.period.period
"""
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
class SoruListesi(models.Model):
    sorular=models.CharField(max_length=200,default="")
    def __str__(self): 
        return self.sorular
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
"""