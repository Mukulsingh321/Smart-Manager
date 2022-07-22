import random
import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import auth
from django.contrib.sessions.models import Session
from datetime import datetime
from django.views.generic import ListView, UpdateView, CreateView
from django.core.mail import send_mail
from django.contrib.messages import add_message
from django.core.validators import ValidationError
from django.core.mail import send_mail
from django.conf import settings
import uuid


def home(request):
    user = User.objects.all()
    print('your mail id is :', request.session.get('username'))
    print('your role id is :', request.session.get('role_id'))
    print('your role ids is :', request.session.get('role_ids'))
    print('Your password is: ', request.session.get('password'))
    role_id = request.session.get('role_id')
    role_ids = request.session.get('role_ids')
    mail_id = request.session.get('username')
    pawd = request.session.get('password')
    # print(role_id, 'this os role_id secondd')
    rol = role_master.objects.filter(role_id__in=role_ids)
    if request.method == 'GET':
        ro = request.GET.get('role_name')
    for i in rol:
        print(i.role_id, 'this is i')
    print(ro, 'this is ro')

    superusers = User.objects.filter(is_superuser=True)
    print(superusers, 'this is superuser')
    # log_emp = login_emp.objects.filter()
    context = {
        'user': user,
        'role_id': role_id,
        'role_ids': role_ids,
        'mail_id': mail_id,
        'rol': rol,
        'ro': ro,
        'pawd': pawd
    }
    return render(request, 'index.html', context)


def tech(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        if technology_master.objects.filter(name=name).exists():
            messages.error(request, f'{name} already exists')
            return HttpResponse('Hello')
        else:
            n = technology_master(name=name, desc=desc)
            n.save()
            messages.success(request, "Technology added Successfully")
            return HttpResponse('Bye')

    elif request.method == 'GET':
        return render(request, 'add_tech.html')
    else:
        return render(request, 'add_tech.html')


def tech_list(request):
    tech_mas = technology_master.objects.all()
    context = {
        'tech_mas': tech_mas
    }
    return render(request, 'tech_list.html', context)

def edit_tech(request, num):
    tms = technology_master.objects.get(tech_id=num)
    if request.method == 'POST':
        tms.name = request.POST.get('name')
        tms.desc = request.POST.get('desc')
        active_status = request.POST.get('checkbox')
        if active_status == None:
            tms.active_status = request.POST = False
        else:
            tms.active_status = request.POST = True
        tms.save()
        messages.success(request, 'Technology Edit Successfully')
    return render(request, 'edit_tech.html', {'tms': tms})


def tech_emp(request):
    emp = employee.objects.all()
    tech = technology_master.objects.all()
    context = {
        'emp': emp,
        'tech': tech
    }
    if request.method == 'POST':
        e = emp_tech()
        e.emp_id_id = request.POST.get('employee')
        e.tech_id = request.POST.get('tech_name')
        e.save()
        messages.success(request, 'Employee Technology Added Successfully')
    elif request.method == 'GET':
        return render(request, 'emp_tech.html', context)
    return render(request, 'emp_tech.html', context)


def emp_tech_list(request):
    tech_emp = emp_tech.objects.all()
    return render(request, 'emp_tech_list.html', {'emp': tech_emp})



def role(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        if role_master.objects.filter(name=name).exists():
            messages.error(request, f'{name} already exists')
        else:
            new = role_master(name=name, desc=desc)
            new.save()
            messages.success(request, "Role added Successfully")
    elif request.method == 'GET':
        return render(request, 'add_role.html')
    return render(request, 'add_role.html')


def emp_rol_edit(request,num):
    emp_rol = emp_role.objects.get(emp_role_id= num)
    emp = employee.objects.all()
    rol = role_master.objects.all()
    context = {
        'emp_rol': emp_rol,
        'emp': emp,
        'rol': rol
    }
    return render(request, 'emp_role_edit.html', context)



def role_list(request):
    role_mas = role_master.objects.all()
    context = {
        'role_mas': role_mas
    }
    return render(request, 'role_list.html', context)


def role_emp(request):
    rol = role_master.objects.all()
    emp = (employee.objects.all())
    context = {
        'emp': emp,
        'rol': rol
    }
    if request.method == 'POST':
        # emp_id_id = request.POST.get('employee')
        role = request.POST.getlist('role_name')
        rol = ([int(x) for x in role])
        for i in rol:
            r = emp_role()
            r.emp_id_id = request.POST.get('employee')
            r.role_id_id = i
            if emp_role.objects.filter(role_id_id=r.role_id_id, emp_id=r.emp_id_id).exists():
                messages.error(request,f'{r.emp_id} Already plays {r.role_id} Role')
            else:
                r.save()
                messages.success(request, 'Employee Role Registred Successfully')
    elif request.method == 'GET':
        return render(request, 'emp_role.html', context)
    return render(request, 'emp_role.html', context)


def emp_rol_list(request):
    emp_rol = emp_role.objects.all()
    return render(request, 'emp_role_list.html', {'rol': emp_rol})



# def role_emp(request):
#     rol = role_master.objects.all()
#     emp = employee.objects.all()
#     print(list(emp))
#     context= {
#         'emp':emp,
#         'rol':rol
#     }
#     if request.method == 'POST':
#         emp_id_id = request.POST.get('employee')
#         role = request.POST.getlist('role_name')
#         rol = ([int(x) for x in role])
#         emp_rol = emp_role.objects.create(emp_id_id=emp_id_id)
#         for x in rol:
#             emp_rol.role_id.add(role_master.objects.get(role_id=x))
#         messages.success(request, 'Employee Role Added Successfully')
#
#         if emp_role.objects.filter(role_id=([p for p in emp_role.role_id.all()])).exists():
#             messages.error(request, f'{emp_id_id.first_name} Already Plays {emp_rol.role_id} Role')
#         # else:
#         #     messages.success(request,'Employee Role Added Successfully')
#     elif request.method == 'GET':
#         return render(request,'emp_role.html',context)
#     return render(request,'emp_role.html',context)



def role_edit(request, id):
    roll = role_master.objects.get(role_id=id)
    if request.method == 'POST':
        roll.name = request.POST.get('name')
        roll.desc = request.POST.get('desc')
        active_status = request.POST.get('checkbox')
        if active_status == None:
            roll.active_status = request.POST = False
        else:
            roll.active_status = request.POST = True
        roll.save()
        messages.success(request, 'Role Edit Successfully')
    elif request.method== 'GET':
        return render(request, 'edit_role.html',{'roll':roll})
    return render(request, 'edit_role.html', {'roll': roll})


def add_emp(request):
    state = state_master.objects.all()
    city = city_master.objects.all()
    tech = technology_master.objects.all()
    role = role_master.objects.all()
    emp = employee.objects.all()

    if request.method == 'POST':
        emp_code = request.POST.get('emp_code')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = int(request.POST.get('mobile'))
        alternate = int(request.POST.get('alternate'))
        email = request.POST.get('email')
        # p.emp_tech = technology_master.objects.get(tech_id=request.POST.get("tech_name"))
        # p.emp_role = role_master.objects.get(role_id=request.POST.get("role_name"))
        r_address = request.POST.get('r_addrerss')
        r_state = state_master.objects.get(SID=request.POST.get("state"))
        r_city = city_master.objects.get(CTID=request.POST.get("city"))
        p_address = request.POST.get('p_address')
        p_state = state_master.objects.get(SID=request.POST.get("state1"))
        p_city = city_master.objects.get(CTID=request.POST.get("city1"))
        image = request.FILES.get('image')
        join_date = request.POST.get("join_date")
        if employee.objects.filter(emp_code=emp_code, email=email).exists():
            messages.error(request, f'Email : {emp_code} Already Exists')
        else:
            character = list('abcdefghijklmnopqrstuvwxyz')
            length = 4
            pas = ''
            for x in range(length):
                pas+=random.choice(character)
                print(pas, 'this is pas')
                request.session['password']= pas

            user = User.objects.create_user(username=email, password=pas)
            employee.objects.create(user=user, first_name=first_name, last_name=last_name, emp_code=emp_code, mobile=mobile, alternate=alternate, email=email, r_address=r_address, r_state=r_state, r_city=r_city, p_address=p_address, p_state=p_state, p_city=p_city, image=image, join_date=join_date)
            messages.success(request, f'{first_name} Added Successfully and your password is {pas}')
            return HttpResponseRedirect('/emp_role/')

    elif request.method == 'GET':
        return render(request, 'add_emp.html', {'state': state,
                                                'city': city,
                                                'tech': tech,
                                                'role': role,
                                                "emp": emp})

    return render(request, 'add_emp.html', {'state': state,
                                            'city': city,
                                            'tech': tech,
                                            'role': role,
                                            'emp': emp})


# def add_emp(request):
#     state = state_master.objects.all()
#     city = city_master.objects.all()
#     tech = technology_master.objects.all()
#     role = role_master.objects.all()
#     emp = employee.objects.all()
#
#     if request.method == 'POST':
#         p = employee()
#         p.emp_code = request.POST.get('emp_code')
#         p.first_name = request.POST.get('first_name')
#         p.last_name = request.POST.get('last_name')
#         p.mobile = int(request.POST.get('mobile'))
#         p.alternate = int(request.POST.get('alternate'))
#         p.email = request.POST.get('email')
#         # p.emp_tech = technology_master.objects.get(tech_id=request.POST.get("tech_name"))
#         # p.emp_role = role_master.objects.get(role_id=request.POST.get("role_name"))
#         p.r_address = request.POST.get('r_addrerss')
#         p.r_state = state_master.objects.get(SID=request.POST.get("state"))
#         p.r_city = city_master.objects.get(CTID=request.POST.get("city"))
#         p.p_address = request.POST.get('p_address')
#         p.p_state = state_master.objects.get(SID=request.POST.get("state1"))
#         p.p_city = city_master.objects.get(CTID=request.POST.get("city1"))
#         p.image = request.FILES.get('image')
#         p.join_date = request.POST.get("join_date")
#         if employee.objects.filter(Q(emp_code=p.emp_code) | Q(email=p.email)).exists():
#             messages.error(request, f'Email : {p.emp_code} Already Exists')
#         else:
#             character = list('abcdefghijklmnopqrstuvwxyz')
#             length = 10
#             pas = ''
#             for x in range(length):
#                 pas+=random.choice(character)
#
#             user = User.objects.create_user(username=p.email, password=pas)
#             user.save()
#             p.save()
#             messages.success(request, 'Employee Added Successfully')
#
#     elif request.method == 'GET':
#         return render(request, 'add_emp.html', {'state': state,
#                                                 'city': city,
#                                                 'tech': tech,
#                                                 'role': role,
#                                                 "emp": emp})
#
#     return render(request, 'add_emp.html', {'state': state,
#                                             'city': city,
#                                             'tech': tech,
#                                             'role': role,
#                                             'emp': emp})



def load_cities(request):
    state_id = request.GET.get('state0')
    cities = city_master.objects.filter(SID=state_id)
    return render(request, 'city_dropdown.html', {'cities': cities})



def emp_list(request):
    emp = employee.objects.all()
    log_emp = request.session.get('password')
    context = {
        'emp': emp,
        'log_emp': log_emp
    }
    return render(request, 'emp_list.html', context)


def edit_emp(request, num):
    state = state_master.objects.all()
    emp = employee.objects.all()
    city = city_master.objects.all()
    tech = technology_master.objects.all()
    role = role_master.objects.all()
    ed_emp = get_object_or_404(employee, emp_code=num)
    context = {
        'state': state,
        'city': city,
        'tech': tech,
        'role': role,
        'ed_emp': ed_emp,
        'emp': emp
    }

    if request.method == 'POST':
        ed_emp.emp_code = request.POST.get('emp_code')
        ed_emp.first_name = request.POST.get('first_name')
        ed_emp.last_name = request.POST.get('last_name')
        ed_emp.mobile = int(request.POST.get('mobile'))
        ed_emp.alternate = int(request.POST.get('alternate'))
        ed_emp.email = request.POST.get('email')
        ed_emp.r_address = request.POST.get('r_addrerss')
        ed_emp.r_state = state_master.objects.get(SID=request.POST.get("state"))
        ed_emp.r_city = city_master.objects.get(CTID=request.POST.get("city"))
        ed_emp.p_address = request.POST.get('p_address')
        ed_emp.p_state = state_master.objects.get(SID=request.POST.get("state1"))
        ed_emp.p_city = city_master.objects.get(CTID=request.POST.get("city1"))
        ed_emp.join_date = request.POST.get("join_date")
        ed_emp.image = request.FILES.get("image")
        emp_status = request.POST.get('checkbox')
        if emp_status == None:
            ed_emp.emp_status = request.POST = False
        else:
            ed_emp.emp_status = request.POST = True
        ed_emp.save()
        messages.success(request, "Employee Edit Successfully")
    return render(request, 'edit_emp.html', context)


def show_img(request):
    emp = employee.objects.get(emp_code='QC001')
    user = User.objects.all()
    return render(request, 'img.html', {'emp': emp, 'user': user})


def login(request):
    userr = User.objects.all()
    role = role_master.objects.all()
    context = {
        'userr': userr,
        'role': role
    }
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            messages.success(request, 'Login Successfully')
            emp = emp_role.objects.filter(emp_id__email__contains=user.username) #use to get employee role with input in email
            print(emp, 'this is emp')
            emp_id = emp_role.objects.filter(emp_id__email__contains= user.username)
            print(emp_id, 'this is emp')
            emp_idd = ''
            for i in emp_id:
                emp_idd = i.emp_id.emp_code
            employe = employee.objects.get(emp_code=emp_idd)
            login_emp.objects.create(emp_id=employe, username=username, password=password)

            # Store only one id into session

            # rol = ''
            # for i in emp:
            #     rol = i.role_id
            # print(rol, 'this is rol')
            # # data = serializers.serialize('json', emp)
            # if user:
            #     request.session['username'] = user.username
            #     request.session['role_id'] = rol.role_id
            # print(request.user.username, 'this is request user username')

            # Store more than one id into session

            # lst =[]
            # for i in emp:
            #     i.role_id.role_id
            #     lst.append(i.role_id.role_id)
            # print(lst, 'this is list')
            # if user:
            #     request.session['username'] = user.username
            #     request.session['role_id'] = lst

            lst = []
            for i in emp:
                i.role_id.role_id
                lst.append(i.role_id.role_id)
            tup = tuple(lst)
            print(tup, 'this is list')
            if user:
                request.session['username'] = user.username
                request.session['role_id'] = tup[0]
                request.session['role_ids'] = tup
                request.session['pawd']=password

        if (user is not None):
            messages.error(request, 'Login Successfully')
            return HttpResponseRedirect("/index/")
        else:
            messages.error(request, "Invalid Username and Password")
    elif request.method == 'GET':
        return render(request, 'login_page.html', context)
    return render(request, 'login_page.html', context)


def forgot_pass(request):
    # pas =
    # subject = 'Your Change Password Link'
    # message = 'Your new password is : '
    char = 'abcdefghijklmopqrstuvwxyz'
    length = 4
    pas = ''
    for i in range(length):
        pas += random.choice(char)
    if request.method == 'POST':
        pasw = request.POST.get('email')
        user = User.objects.filter(email__exact=pasw)
        # user.set_password(pas)
        # user.save()
        print(pas, 'this is new password')
    return render(request, 'forgot-pass.html')


def profile(request):
    return render(request, 'profile.html')


def fake(request):
    emp = employee.objects.all()
    return render(request, 'fake.html', {'emp': emp})


def logout_view(request):
    try:
        del request.session['username']
        del request.session['role_id']
        del request.sessiom['password']
        messages.success(request, 'Logout Successfully')
    except:
        messages.error(request,"Logout Successfully")
        return redirect('/')
    return redirect('/')

def get_sesion(request):
    user = request.session.keys()
    return render(request, 'img.hmtl', {'user': user})


def add_client(request):
    state = state_master.objects.all()
    city = city_master.objects.all()
    context = {
        'state': state,
        'city': city
    }

    if request.method == 'POST':
        c = Client()
        c.company_name = request.POST.get('comp_name')
        c.first_name = request.POST.get('first_name')
        c.last_name = request.POST.get('last_name')
        c.mobile = int(request.POST.get('mobile'))
        c.alternative = request.POST.get('alternate')
        c.email = request.POST.get('email')
        c.state_id = state_master.objects.get(SID=request.POST.get("state"))
        c.city_id = city_master.objects.get(CTID=request.POST.get("city"))
        c.join_date = request.POST.get('join_date')
        if Client.objects.filter(company_name=c.company_name).exists():
            messages.error(request, f'{c.company_name} Already Exists')
        else:
            messages.success(request, 'Client Added Succeessfully')
            c.save()
    elif request.method == 'GET':
        return render(request, 'add_client.html', context)
    return render(request, 'add_client.html', context)


def client_list(request):
    client = Client.objects.all()
    context = {
        'client': client
    }
    return render(request, 'client_list.html', context)



def edit_client(request, num):
    ed_cl = Client.objects.get(client_id=num)
    clients = Client.objects.all()
    state = state_master.objects.all()
    city = city_master.objects.all()
    context = {
        'client': clients,
        'ed_cl': ed_cl,
        'state': state,
        'city': city,
    }
    if request.method == 'POST':
        ed_cl.comany_name = request.POST.get('comp_name')
        ed_cl.first_name = request.POST.get('first_name')
        ed_cl.last_name = request.POST.get('last_name')
        ed_cl.mobile = request.POST.get('mobile')
        ed_cl.alternative = request.POST.get('alternate')
        ed_cl.email = request.POST.get('email')
        ed_cl.state_id = state_master.objects.get(SID=request.POST.get("state"))
        ed_cl.city_id = city_master.objects.get(CTID=request.POST.get("city"))
        ed_cl.join_date = request.POST.get('join_date')
        active_status = request.POST.get('checkbox')
        if active_status == None:
            ed_cl.active_status = request.POST = False
        else:
            ed_cl.active_status = request.POST = True
        ed_cl.save()
        messages.success(request, 'Client Edited Successfully')
    elif request.method == 'GET':
        return render(request, 'edit_client.html', context)
    return render(request, 'edit_client.html', context)


def add_proj(request):
    client = Client.objects.all()
    if request.method == 'POST':
        p = Project()
        p.client_id_id = request.POST.get('client')
        p.project_name = request.POST.get('proj_name')
        p.start_date = request.POST.get('start_date')
        p.end_date = request.POST.get('end_date')
        if Project.objects.filter(client_id=p.client_id_id, project_name=p.project_name).exists():
            messages.error(request, f'{p.project_name} Already Exists')
        else:
            messages.success(request, 'Project Added Successfully')
            p.save()
    elif request.method == 'GET':
        return render(request, 'add_project.html', {'client': client})
    return render(request, 'add_project.html', {'client': client})


def proj_list(request):
    proj = Project.objects.all()
    projt= ProjectTeam.objects.all()
    context = {
        'proj': proj,
        'projt': projt,
    }
    return render(request, 'proj_list.html', context)



def edit_proj(request, num):
    proj = Project.objects.all()
    client = Client.objects.all()
    p = Project.objects.get(proj_id=num)
    context = {
        'proj': proj,
        'client': client,
        'p': p
    }
    if request.method == 'POST':
        p.client_id_id = request.POST.get('client')
        p.project_name = request.POST.get('proj_name')
        p.start_date = request.POST.get('start_date')
        p.end_date = request.POST.get('end_date')
        active_status = request.POST.get('checkbox')
        if active_status == None:
            p.active_status = request.POST = False
        else:
            p.active_status = request.POST = True
        p.save()
        messages.success(request, 'Project Edit Successfully')

    elif request.method == 'GET':
        return render(request, 'edit_proj.html', context)

    return render(request, 'edit_proj.html', context)


def proj_team(request):
    projt = Project.objects.all()
    emp_rol = emp_role.objects.all()
    pt = ProjectTeam.objects.all()

    context = {
        'projt': projt,
        'emp_rol': emp_rol,
        'pt': pt
    }
    if request.method == 'POST':
        # p.project_id_id = request.POST.get(project_id = num)
        employee_role = request.POST.getlist('role_name')
        emp = ([int(x) for x in employee_role])
        for e in emp:
            pt = ProjectTeam()
            pt.project_id_id = request.POST.get('proj')
            pt.employee_role_id_id = e
            pt.assign_date = request.POST.get('assign_date')
            pt.estimate_date = request.POST.get('est_date')
            pt.est_end_date = request.POST.get('est_end_date')
            pt.save()
            messages.success(request, 'Project Added Successfully')
            # if ProjectTeam.objects.filter(employee_role_id=pt.employee_role_id).exists():
            #     messages.error(request, f'{pt.employee_role_id} Already in {pt.project_id}')

        # add_team = ProjectTeam.objects.create(
        #     project_id_id = project_id_id,
        #     assign_date = assign_date,
        #     estimate_date = estimate_date,
        #     est_end_date = est_end_date
        # )
        # for x in emp:
        #     add_team.employee_role_id.add(emp_role.objects.get(emp_role_id = x))
    elif request.method == 'GET':
        return render(request, 'proj_team.html', context)

    return render(request, 'proj_team.html', context)

# def proj_team_list(request):
#     proj_team = ProjectTeam.objects.all()
#     lst = []
#
#     for p in proj_team:
#         a = p.project_id
#         if a not in lst:
#             lst.append(a)
#     context = {
#         'proj_team': proj_team,
#         'lst': lst
#     }
#     print(lst, 'this is list')
#
#     return render(request, 'proj_team_list.html', context)


def proj_view(request, num):
    ptf = ProjectTeam.objects.filter(project_id=num)

    return render(request, 'proj_view.html', {'proj_team': ptf})


def assign_task(request):
    proj = Project.objects.all()
    rol = emp_role.objects.all()
    context = {
        'proj': proj,
        'rol': rol
    }
    return render(request, 'assign_task.html', context)