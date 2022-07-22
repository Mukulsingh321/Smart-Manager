"""smart_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from smart_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('index/', views.home),
    path('add_tech/', views.tech),
    path('tech_list/', views.tech_list),
    path('edit_tech/<int:num>/', views.edit_tech),
    path('add_role/', views.role),
    path('role_list/', views.role_list),
    path('edit_role/<int:id>/', views.role_edit),
    path('add_emp/', views.add_emp),
    path('add_emp/<int:num>/', views.add_emp),
    path('emp_list/', views.emp_list),
    path('edit_emp/<str:num>/', views.edit_emp),
    path('profile/', views.profile),
    path('fake/', views.fake),
    path('logout/', views.logout_view, name='logout'),
    path('add_client/', views.add_client),
    path('client_list/', views.client_list),
    path('edit_client/<int:num>/', views.edit_client),
    path('emp_tech/', views.tech_emp),
    path('emp_role/', views.role_emp),
    path('emp_role_edit/<int:num>/', views.emp_rol_edit),
    path('add_proj/', views.add_proj),
    path('edit_proj/<int:num>/', views.edit_proj),
    path('proj_list/', views.proj_list),
    path('proj_team/', views.proj_team),
    # path('proj_team_list/', views.proj_team_list),
    path('proj_view/<int:num>/', views.proj_view),
    path('assign_task/', views.assign_task),
    path('emp_rol_list/', views.emp_rol_list),
    path('emp_tech_list/', views.emp_tech_list),
    path('forgot/', views.forgot_pass),
    # path('proj_team/<int:num>/', views.proj_team),
    path('img/', views.show_img),
    # path('emp_list/', views.emp_list),

    path('load-cities/', views.load_cities, name='ajax_load_cities'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
