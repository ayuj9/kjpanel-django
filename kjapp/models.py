from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
# Create your models here.


class Client(models.Model):
 
    DIET_CHOICES = {
        'Vegetarian' :"Vegetarian",
        'Non-Vegetarian' : "Non-Vegetarian" ,
        'Vegan' :  "Vegan"
    }
    name = models.CharField(max_length =255)
    age = models.PositiveSmallIntegerField(null=True  )
    phone = models.CharField(max_length =12 , unique = True)
    email = models.EmailField(unique = True)
    diet_language= models.CharField(max_length=255 , null =True)
    gender = models.CharField(max_length = 10)
    diet_preference = models.CharField(max_length = 15 , choices = DIET_CHOICES )
    note = models.TextField(null =True , blank = True)
    # file =models.FileField(upload_to='uploads/', max_length=255 , null=True , default=None )
    
    def __str__(self):
        return self.file.name
   

class FileUpload(models.Model):
    file = models.FileField(upload_to='kjapp/images' , validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    client = models.ForeignKey(Client , on_delete=models.CASCADE , null=True , blank=True , related_name='files' )


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
    duration = models.IntegerField()
    client = models.ForeignKey(Client , on_delete=models.CASCADE,  null=False , blank=False , related_name ="plan")

class Client_Insights(models.Model):
    target_weight = models.CharField(max_length = 10 , null =True)
    height = models.CharField(max_length = 10)
    current_weight = models.CharField(max_length = 10)
    time = models.DateTimeField(default = timezone.now)
    last_plan_updated_timestamp = models.DateTimeField(default=timezone.now)
    persona =models.CharField(max_length=50 , null =True , blank = True)
    height_Unit  = models.CharField(max_length=6 , default="inch")
    weight_Unit  = models.CharField(max_length=2, default="kg")
    client = models.ForeignKey(Client , on_delete=models.CASCADE , null=False , blank=False, related_name='insights')
    


class Diet_Plan(models.Model):
    meal_Time = models.JSONField(null= True, blank = True)
    day1 = models.JSONField( null= True, blank = True,)
    day2 = models.JSONField( null= True, blank = True,)
    day3 = models.JSONField( null= True, blank = True,)
    day4 = models.JSONField( null= True, blank = True,)
    day5 = models.JSONField( null= True, blank = True,)
    day6 = models.JSONField( null= True, blank = True,)
    day7 = models.JSONField( null= True, blank = True)
    note = models.CharField(max_length =255 , null= True, blank = True )
    time = models.DateTimeField(default = timezone.now)
    client = models.ForeignKey(Client , on_delete=models.CASCADE, related_name="diet" )
    

    

class RecipeData(models.Model):
    id = models.IntegerField(primary_key =True)
    name = models.CharField(max_length = 150)
    recipieLink = models.URLField(max_length=200 , null = True , blank =True)




   
    

