# Ex02 Django ORM Web Application
## Date: 05.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Untitled drawing.jpg>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

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

admin.py

from django.contrib import admin
from .models import people,peopleAdmin
admin.site.register(people,peopleAdmin)
```


## OUTPUT
![alt text](<Screenshot 2024-11-05 174837.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
