from django.db import models
from django.contrib import admin
class people(models.Model):
       Name=models.CharField(max_length=15)
       Aadharno=models.IntegerField(primary_key="Aadharno")
       address=models.CharField(max_length=20)
       loanamt=models.IntegerField()
       Email=models.EmailField()
class peopleAdmin(admin.ModelAdmin):
       list_display=('Name','Aadharno','address','loanamt','Email')