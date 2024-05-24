from django.db import models
from django.utils import timezone
# Create your models here.
class Client(models.Model):
 
    DIET_CHOICES = {
        'V' :"Vegetarian",
        'N' : "Non-Vegetarian" ,
        'G' :  "Vegan"
    }
    name = models.CharField(max_length =255)
    age = models.PositiveSmallIntegerField()
    phone = models.CharField(max_length =12 , unique = True)
    email = models.EmailField(unique = True)
    diet_language= models.CharField(max_length=255 , null =True)
    gender = models.CharField(max_length = 1)
    diet_preference = models.CharField(max_length = 1 , choices = DIET_CHOICES )

   

class Address(models.Model):
    city = models.CharField(max_length =255)
    state = models.CharField(max_length =255)
    country =models.CharField(max_length =255)
    client = models.OneToOneField(Client , on_delete=models.CASCADE , related_name = "address")


class Client_Plan(models.Model):

    PLAN_LEVEL_CHOICES =[
        ('B' , 'Bronze'),
        ('S' , 'Silver'),
        ('G' , 'Gold'),
    ]

    STATUS_CHOICES = [
        ('Created' , 'Create'),
        ('Active' , 'Activate'),
        ('Paused' , 'Pause'),
        ('Suspended' , 'Suspend'),
        ('Expired' , 'Expired'),

    ]
    last_plan_updated_timestamp = models.DateTimeField(default=timezone.now)
    start_time = models.DateField(null=False, blank=False)
    end_time = models.DateField(null =False , blank =False)
    plan_level = models.CharField(max_length = 20, choices =PLAN_LEVEL_CHOICES  )   
    status = models.CharField(max_length = 20 , choices = STATUS_CHOICES  )
    target_weight = models.CharField(max_length = 10 , null =True)
    client = models.ForeignKey(Client , on_delete=models.CASCADE,  null=False , blank=False , related_name ="plan")

class Client_Insights(models.Model):
    height = models.CharField(max_length = 10)
    current_weight = models.CharField(max_length = 10)
    note = models.TextField(null =True , blank = True)
    duration = models.CharField(max_length=40)
    time = models.DateTimeField(default = timezone.now)
    last_plan_updated_timestamp = models.DateTimeField(default=timezone.now)
    persona =models.CharField(max_length=50 , null =True , blank = True)
    height_Unit  = models.CharField(max_length=6 , default="inch")
    weight_Unit  = models.CharField(max_length=2, default="kg")
    client = models.ForeignKey(Client , on_delete=models.CASCADE , null=False , blank=False, related_name='insights')



class Diet_Plan(models.Model):
    day1 = models.JSONField(null=True)
    day2 = models.JSONField(null=True)
    day3 = models.JSONField(null=True)
    day4 = models.JSONField(null=True)
    day5 = models.JSONField(null=True)
    day6 = models.JSONField(null=True)
    day7 = models.JSONField(null=True)
    time = models.DateTimeField(default = timezone.now)
    client = models.ForeignKey(Client , on_delete=models.CASCADE , null=False , blank=False)
    

    





   
    

