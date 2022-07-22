from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin


#Create your models here.




class technology_master(models.Model):
    tech_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    active_status = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.name

class emp_tech(models.Model):
    emp_id = models.ForeignKey('employee',on_delete=models.CASCADE)
    tech = models.ForeignKey(technology_master,on_delete=models.CASCADE)
    active_status = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.tech.name


class role_master(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    active_status = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.name

class emp_role(models.Model):
    emp_role_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey(role_master, on_delete=models.CASCADE,null=True)
    emp_id = models.ForeignKey('employee', on_delete=models.CASCADE)
    active_status = models.BooleanField(default=True, null=True)

    def __str__(self):
        return '%s %s' % (self.emp_id, self.role_id)

    # def role(self):
    #     return ",".join([str(p) for p in self.role_id.all()])


class state_master(models.Model):
    SID = models.IntegerField(primary_key=True,default='')
    stateName = models.CharField(max_length=19)

    def __str__(self):
        return self.stateName


class city_master(models.Model):
    CTID = models.IntegerField(primary_key=True,default='')
    SID = models.ForeignKey(state_master,on_delete=models.CASCADE)
    cityName = models.CharField(max_length=24)

    def __str__(self):
        return self.cityName


class employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    emp_id = models.AutoField(primary_key=True)
    emp_code = models.CharField(max_length=100,null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    mobile = models.BigIntegerField()
    alternate = models.BigIntegerField(null=True,blank=True)
    email = models.EmailField()
    r_address = models.CharField(max_length=100,null=True)
    r_state = models.ForeignKey(state_master, on_delete=models.CASCADE,related_name='r_state', null=True,blank=True)
    r_city = models.ForeignKey(city_master, on_delete=models.CASCADE,related_name='r_city', null=True,blank=True)
    p_address = models.CharField(max_length=100,null=True)
    p_state = models.ForeignKey(state_master, on_delete=models.CASCADE,related_name='p_state', null=True,blank=True)
    p_city = models.ForeignKey(city_master, on_delete=models.CASCADE,related_name='p_city', null=True,blank=True)
    join_date = models.DateField(null=True)
    emp_status = models.BooleanField(default=True, null=True, blank=True)
    image = models.ImageField(upload_to='images/',default=None, null=True,blank=True)

    def __str__(self):
        return self.first_name

class login_emp(models.Model):
    user_id = models.AutoField(primary_key = True)
    emp_id = models.ForeignKey('employee', on_delete=models.CASCADE,null=True)
    username = models.EmailField()
    password = models.CharField(max_length=200)
    last_login = models.DateTimeField(auto_now=True)
    active_status = models.BooleanField(default=True, null=True)


    def __str__(self):
        return self.username


class Client(models.Model):
    client_id = models.AutoField(primary_key= True)
    company_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    alternative = models.BigIntegerField()
    email = models.EmailField(null=True)
    state_id = models.ForeignKey(state_master,on_delete=models.CASCADE)
    city_id = models.ForeignKey(city_master,on_delete=models.CASCADE)
    join_date = models.DateTimeField(null=True,blank=True)
    active_status = models.BooleanField(default = True, null=True)

    def __str__(self):
        return self.company_name

class Project(models.Model):

    CHOICES = (
        ('ACTIVE', 'ACTIVE'),
        ('COMPLETED', 'COMPLETED'),
        ('PENDING', 'PENDING'),
        ('SCHEDULED', 'SCHEDULED'),
    )



    proj_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    active_status = models.BooleanField(default=True, null=True)
    proj_status = models.CharField(max_length=9, choices=CHOICES, default='ACTIVE', null=True)

    def __str__(self):
        return self.project_name

class ProjectTeam(models.Model):
    team_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee_role_id = models.ForeignKey(emp_role, on_delete=models.CASCADE, null=True)
    assign_date = models.DateField(null=True, blank=True)
    estimate_date = models.DateField(null=True, blank=True)
    est_end_date = models.DateField(null=True, blank=True)
    active_status = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.project_id.project_name

    # def Employee_role(self):
    #     return ",".join([str(s) for s in self.employee_role_id.all()])