from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
    



class Song(models.Model):
    PUBLIC = "PB"
    PRIVATE = "PR"
    PROTECTED = "PT"
    Title = models.CharField(max_length=20)
    Thumbnail = models.ImageField(default='',null=False,blank=False,upload_to = 'images/%Y/%m')
    songFile =  models.FileField(upload_to="uploads/%Y/%m/%d/")
    Access_choices = [
        (PUBLIC, "PB"),
        (PRIVATE, "PR"),
        (PROTECTED, "PT"),
    ]
    access = models.CharField(
        max_length=2,
        choices=Access_choices,
        default=PUBLIC,
    )            
    user = models.ForeignKey(User,editable=True,blank=True,null=True,on_delete=models.CASCADE)

def __str__(self) -> str:
        return self.email
