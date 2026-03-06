from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('admin/',     admin.site.urls),
    path('login/',     auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',    auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard,  name='dashboard'),
    path('reports/',   views.reports,    name='reports'),
    path('settings/',  views.settings,   name='settings'),
    path('new-employee/',  views.new_employee_settings,   name='new_employee_settings'),
]