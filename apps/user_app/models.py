from django.db import models

# Create your models here.
from django.contrib.auth. models import AbstractUser


class DistricModel(models.Model):
    district_name =models.CharField(max_length=50)

class TownModel(models.Model):
    district= models.ForeignKey(DistricModel, on_delete=models.CASCADE)
    town= models.CharField(max_length=50)

class UserModel(AbstractUser):

    ADMINS='ADMINS'
    NORMA_USER= "NORMAL_USER"
    USER_CHOICES=(
        (ADMINS ,'admins'),
        (NORMA_USER, 'jwelbix_user')
    )

    ACTIVE= 'ACTIVE'
    DEACTIVATED= 'DEACTIVATED'
    STATUS_CHOICE= (
        (ACTIVE, 'active'),
        (DEACTIVATED, 'deactivated')
    )

    mobile_no= models.CharField(max_length=15, null=True)
    lat= models.CharField(max_length=100)
    lon= models.CharField(max_length=100)
    user_type= models.CharField(max_length=20, choices=USER_CHOICES,default='jwelbix_user')
    status= models.CharField(max_length=100, choices=STATUS_CHOICE, default='active')
    district= models.ForeignKey(DistricModel, on_delete=models.CASCADE,null=True, blank=True)
    town= models.ForeignKey(TownModel, on_delete=models.CASCADE, blank=True, null=True)
    is_verified= models.BooleanField(default= True)
    fcm_token= models.CharField(max_length=200, blank=True, null=True)







     
