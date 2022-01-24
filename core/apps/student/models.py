from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from django.db.models.fields.related import OneToOneField,ManyToManyField
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator,ValidationError
import os

# Create your models here.
from ..home.models import Profil,Session,Period
from ..classes.models import Classes

def validateHesCode(value):
    HesCodeRegex = RegexValidator(regex=r'^[0-9]{4}-?[0-9]{5}$', message="HES Code  must be entered in the format: 'Txxx-xxxx-x'. Up to 9  char allowed.")
def validatePhone(value):
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
def validateEven(value):
    y=str(value)
    x=list(y)
        
        
    if len(x) != 11:
        raise ValidationError(
            ('%(value)s 11 basasmaklı olmalı'),
            params={'value': value},
        )
class MiddleSchool(models.Model):
    name=models.CharField(max_length=100,default="")
    def __str__(self): 
        return self.name

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(instance.TC), ext)
    return os.path.join('images/ogrenciler/', filename)

class Student(models.Model):
    firstName= models.CharField(max_length=20,default="",unique=False,null=True,blank=True,)
    lastName=models.CharField(max_length=20,unique=False,null=True,blank=True,)
    TC = models.CharField(max_length=11,unique=False,null=True,blank=True,validators=[validateEven])
    phone = models.CharField(validators=[validatePhone], max_length=17,default="0",unique=False,null=True,blank=True,)
    address=models.TextField(unique=False,null=True,blank=True,)
    status=models.BooleanField(unique=False,null=True,blank=True,)
    middleSchool=models.ForeignKey(MiddleSchool,on_delete=models.CASCADE)
    number=models.IntegerField(unique=False,null=True,blank=True,)
    session=models.ForeignKey(Session,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=upload_location,unique=False,null=True,blank=True,default='images/person.png')
    health=models.TextField(unique=False,null=True,blank=True,)
    HESCode=models.CharField(max_length=12,unique=False,null=True,blank=True,validators=[validateHesCode])
    birtdate=DateField(("Doğum Tarihiniz"), auto_now=False, auto_now_add=False,unique=False,null=True,blank=True,)
    email=models.EmailField()
    genders=(('Kız','Kız'),
              ('Erkek','Erkek'),
              ('Diger','Diğer'),
    )
    gender=CharField(max_length=10 ,choices=genders,unique=False,blank=True,null=True)
    class Meta:
        ordering = ('firstName',)
    
    def __str__(self):
        return self.session.session + " - " + str(self.number) +" - " + self.firstName +' '+self.lastName
    def save(self, *args, **kwargs):
        
        if '-' not in self.HESCode and self.HESCode!=None and self.HESCode!="" :
            self.HESCode = '{0}-{1}-{2}'.format(
                 self.HESCode[:4], self.HESCode[4:9], self.HESCode[9:])
        if '-' not in self.phone and self.phone!=None and self.phone!="":
            self.phone = '({0})-{1} {2}'.format(
                 self.phone[:4], self.phone[4:7], self.phone[7:])
        
        # Continue the model saving
        super(Student, self).save(*args, **kwargs)
class Parent(models.Model):
    firstName= models.CharField(max_length=20,default="",unique=False,null=True,blank=True,)
    lastName=models.CharField(max_length=20,default="",unique=False,null=True,blank=True,)
    student=models.ManyToManyField(Student)
    relation=models.CharField(max_length=30,default="",unique=False,null=True,blank=True,)
    phone=models.IntegerField()
    adsreds=models.TextField(max_length=200,default="",unique=False,null=True,blank=True,)
    job=models.CharField(max_length=30,default="",unique=False,null=True,blank=True,)

    def __str__(self):
        return "Veli : " +  self.firstName +' '+ self.lastName  

class StudentList(models.Model):
    className=models.ForeignKey(Classes,on_delete=models.CASCADE)
    session=models.ForeignKey(Session,on_delete=models.CASCADE)
    periods=models.ForeignKey(Period,on_delete=models.CASCADE)
    students=models.ManyToManyField(Student,blank=True)
    mainteacher=models.ForeignKey(Profil,on_delete=models.CASCADE,blank=True,verbose_name="Sınıf Öğretmeni",related_name='teacher',null=True)
    class Meta:
        ordering = ('className',"session","periods",)
    def __str__(self):
        
        return  str(self.session.session)+' '+self.periods.period +' '+str(self.className.level.level)+self.className.className.name
