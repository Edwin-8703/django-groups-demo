from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# This decorator checks if the user belongs to any of the given groups
def group_required(*groups):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            # Superuser can access everything
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            # Check if user is in one of the allowed groups
            if request.user.groups.filter(name__in=groups).exists():
                return view_func(request, *args, **kwargs)
            # Otherwise show access denied
            return render(request, 'accounts/403.html', status=403)
        return wrapper
    return decorator


@login_required
def dashboard(request):
    # All logged in users can see this
    return render(request, 'accounts/dashboard.html')


@group_required('Managers', 'Admins')
def reports(request):
    # Only Managers and Admins can see this
    return render(request, 'accounts/reports.html')


@group_required('Admins')
def settings(request):
    # Only Admins can see this
    return render(request, 'accounts/settings.html')

@group_required('New Employees')
def new_employee_settings(request):
    # Only New Employees can see this
    return render(request, 'accounts/new_employee.html')
