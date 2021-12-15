from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime
# Create your models here.
class Appointment(models.Model):
    name=models.CharField(max_length=50,null=True)
    Email=models.EmailField(max_length=254,null=True)
    Mobile_No=models.CharField(max_length=10,null=True)
    features=(
        ("30","haircut"),
        ("90","hair color"),
        ("89","facial"),
        ("45","oil massage"),
        ("15","threading"),
        ("29","mehendi"),
        ("40","waxing"),
        ("28","nailcare"),
        ("60","makeup"),
    )
    List=MultiSelectField(choices=features)
    condition1= [
    ('appointed', 'appointed'),
    ('not_appointed', 'not_appointed'),
    ('not_verified','not_verified'),
    ]
    condition2= [
    ('rita', 'rita'),
    ('sita', 'sita'),
    ('gita','gita'),
    ]
    selected=models.CharField(max_length=120,choices=condition1,default='not_verified' )
    staff=models.CharField(max_length=120,choices=condition2,default='not_verified' )
    Time=models.TimeField()
    endtime=models.TimeField(null=True)
    Date=models.DateField()
    
