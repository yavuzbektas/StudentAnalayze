from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from django.db.models.fields.related import OneToOneField,ManyToManyField
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator,ValidationError
# Create your models here.
from ..home.models import Session
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

class Student(models.Model):
    firstName= models.CharField(max_length=20,default="",unique=False,null=True,blank=True,)
    lastName=models.CharField(max_length=20,unique=False,null=True,blank=True,)
    TC = models.CharField(max_length=11,unique=False,null=True,blank=True,validators=[validateEven])
    phone = models.CharField(validators=[validatePhone], max_length=17,default="0",unique=False,null=True,blank=True,)
    address=models.TextField(unique=False,null=True,blank=True,)
    status=models.BooleanField(unique=False,null=True,blank=True,)
    middleSchool=models.ForeignKey(MiddleSchool,on_delete=models.CASCADE)
    session=models.ForeignKey(Session,on_delete=models.CASCADE)
    image=models.ImageField(unique=False,null=True,blank=True,upload_to='images',default='https://picsum.photos/200/300')
    health=models.TextField(unique=False,null=True,blank=True,)
    HESCode=models.CharField(max_length=12,unique=False,null=True,blank=True,validators=[validateHesCode])
    birtdate=DateField(("Doğum Tarihiniz"), auto_now=False, auto_now_add=False,unique=False,null=True,blank=True,)
    email=models.EmailField()
    genders=(('Kız','Kız'),
              ('Erkek','Erkek'),
              ('Diger','Diğer'),
    )
    gender=CharField(max_length=10 ,choices=genders,unique=False,blank=True,null=True)
    
    
    def __str__(self):
        return self.firstName +' '+self.lastName
    def save(self, *args, **kwargs):
        
        if '-' not in self.HESCode:
            self.HESCode = '{0}-{1}-{2}'.format(
                 self.HESCode[:4], self.HESCode[4:9], self.HESCode[9:])
        if '-' not in self.phone:
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
