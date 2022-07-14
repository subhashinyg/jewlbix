from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from .models import *

usermodel= get_user_model()
admin.site.register(usermodel)
admin.site.register(TownModel)
admin.site.register(DistricModel)