from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('',            lambda request: redirect('login')),
    path('admin/',     admin.site.urls),
    path('login/',     auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
     path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(http_method_names=['get', 'post']), name='logout'),
    path('dashboard/', views.dashboard,  name='dashboard'),
    path('infoseeker/', views.infoseeker, name='infoseeker'),
    path('infocontributor/', views.infocontributor, name='infocontributor'),
    path('serviceuser/', views.serviceuser, name='serviceuser'),
    path('servicecoor/', views.servicecoor, name='servicecoor'),
    path('leave-application/', views.leave_application, name='leave_application'),
    path('service-request/', views.service_request, name='service_request'),
    path('book-resource/', views.book_resource, name='book_resource'),
    
]