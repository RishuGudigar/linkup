from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class fProfile(models.Model):

    YEAR_CHOICES = [(r,r) for r in range(1960, datetime.date.today().year+1)]

    #Details
    user = models.OneToOneField(User,primary_key=True,verbose_name='user',related_name='profile',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10,null=True)
    operation_commenced = models.IntegerField(('operation_commenced'), choices=YEAR_CHOICES, default=datetime.datetime.now().year,null=True)
    franchise_commenced=models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year,null=True)
    LOGO=models.ImageField(upload_to='franchisor',null=True,default='franchisor/baymax.jpg')
    
    #location Details
    
    city=models.CharField(max_length=30)
   
    #About the Franchise
    about_us=models.TextField(null=True)
    mission=models.TextField(null=True)
    vision=models.TextField(null=True)

    #Franchise Details
    PERCENTAGE_CHOICES=[(r,r) for r in range(1,100)]
    CATEGORY_CHOICES=(('Automotive','Automotive'),('Beauty&Health','Beauty&Health'),('Dealers & Distributers','Dealers & Distributers'),('Education','Education'),('Fashion','Fashion'),('Food and Beverage','Food and Beverage'),('Home Decor','Home Decor'),('Home Based Business','Home Based Business'),('Hotel Travel & Tourism','Hotel Travel & Tourism'),('Retail','Retail'),('Sports,Fitness& Entertainment','Sports,Fitness& Entertainment'))
    category = models.CharField(max_length=1000, choices=CATEGORY_CHOICES,null=True)
    investment=models.IntegerField(null=True)
    brand_fee=models.IntegerField(null=True)
    royalty=models.IntegerField(null=True,choices=PERCENTAGE_CHOICES)

    #Bussiness Details
    PAYBACK_TIME=(('Less than a year','Less than a year'),('1 year','1 year'),('2 years','2 years'),('3 Years','3 Years'),('4 Years','4 Years'),('5 Years','5 Years'),('More than 5 Years','More than 5 Years'))
    anticipated_return_on_investment=models.IntegerField(null=True,choices=PERCENTAGE_CHOICES)
    likely_payback_period=models.CharField(null=True,choices=PAYBACK_TIME,max_length=30)

    #Property Details
    floor_area_required=models.IntegerField(null=True)

    #Employee Details
    employees_requires=models.IntegerField(default=0)

    #Agreement
    YES_NO=(('Yes','Yes'),('No','No'))
    standard_agreement=models.CharField(null=True,choices=YES_NO,max_length=4)
    franchise_term=models.IntegerField(null=True)
    term_renewable=models.CharField(null=True,choices=YES_NO,max_length=4)
    

    def __str__(self):
        return self.name