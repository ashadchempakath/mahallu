from django.db import models
from django import forms
from django.db.models.fields import Field

# Create your models here.


GENDER_CATEGORY = (
    ('MALE','Male'),
    ('FEMALE','Female'),
    ('TRANS','Trans Gender'),
)


MARTIAL_CATEGORY = (
    ('SINGLE','Single'),
    ('MARRIED','Married'),
    ('DIVORCED','Divorced'),
    ('WIDOWED','Widowed'),
)

BLOOD_GROUP = (
    ('A +ve','A +ve'),
    ('B +ve','B +ve'),
    ('AB +ve','AB +ve'),
    ('A -ve','A -ve'),
    ('B -ve','B -ve'),
    ('AB -ve','AB -ve'),
    ('O +ve','O +ve'),
    ('O -ve','O -ve'),
    ('Other','Other'),
   
    )


EDUCATION_CHOICES = (
    ('10TH','10th'),
    ('+2','+2'),
    ('DEGREE','Degree'),
    ('PG','Pg'),
)

class RelationToHomeOwnerform  (forms.Form):
    homerelation_list = [
   'FATHER',
   'MOTHER',
   'SON',
   'DOUGHTER',
   'FATHER IN LAW',
   'MOTHER IN LAW',
   'SON IN LAW',
   'GRAND SON',
   'GRAND DOUGHTER',
    ]
   



class Family(models.Model):
    familyname = models.CharField(max_length=400)
    address  = models.CharField(max_length=2500)
    def __str__(self) -> str:
        return self.familyname
    
class Area(models.Model):
    areaname = models.CharField(max_length=400)
    def __str__(self) -> str:
        return self.areaname
    
class Dprofile(models.Model):
    firstname = models.CharField(max_length=400)
    middlename  = models.CharField(max_length=100,blank=True)
    lastname  = models.CharField(max_length=100,blank=True)
    familyname = models.ForeignKey(Family,on_delete=models.PROTECT)
    Homeowner = models.CharField(max_length=150)
    relationtoHomeowner  = models.CharField(max_length=100)
    fathername = models.CharField(max_length=150) #,related_name="familyname"
   # fathername = models.CharField(max_length=400)
    mothername  = models.CharField(max_length=100)
    motherfamilyname  = models.CharField(max_length=100)
    dateofbirth  = models.DateField()#widget=forms.DateTimeInput(format='%d/%m/%Y')
    age  = models.IntegerField(blank=True, null=True)
    gender  = models.CharField(choices=GENDER_CATEGORY,max_length=20)
    education  = models.CharField(blank=True, null=True,max_length=2000)
    educationcertification  = models.TextField(blank=True, null=True)
    educationislamic  = models.CharField(max_length=1000,blank=True,null=True)
    skill  = models.TextField(blank=True,null=True)
    occupation  = models.CharField(max_length=200,blank=True)
    pravasi  = models.CharField(max_length=100,blank=True,null=True)
    area =  models.ForeignKey(Area,on_delete=models.PROTECT)
    address  = models.CharField(blank=True, null=True,max_length=2000)
    contactno  = models.CharField(max_length=100)
    bloodgroup  = models.CharField(choices=BLOOD_GROUP, max_length=50,blank=True,null=True)
    email  = models.CharField(max_length=100,blank=True,null=True)
    martialstatus  = models.CharField(choices=MARTIAL_CATEGORY,max_length=25)
    spousedetails  = models.CharField(max_length=300,blank=True,null=True)
    spouseoccupation  = models.CharField(max_length=300,blank=True,null=True)
    noofkids  = models.IntegerField(blank=True,null=True)
    disablities  = models.TextField(blank=True, null=True)
    previousmahallu = models.CharField(max_length=100,blank=True,null=True)
    alive  = models.BooleanField(blank=True,null=True)
    dateofdeath  = models.DateField(blank=True,null=True)
    deathreason  = models.TextField(blank=True, null=True)
    covidvaccine = models.CharField(max_length=300,blank=True,null=True)
    otherdetails = models.TextField(blank=True, null=True)
    userid = models.IntegerField()
    lastmodifieduserid = models.IntegerField()
    registrationdate = models.DateField()
    lastmodifieddate = models.DateField()
    










