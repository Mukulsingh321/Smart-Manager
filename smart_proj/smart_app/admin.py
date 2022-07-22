from django.contrib import admin
from .models import *


#Register your models here.
myModel = [technology_master, role_master, state_master, city_master, employee, Client, Project, emp_tech, login_emp, emp_role, ProjectTeam]
admin.site.register(myModel)
