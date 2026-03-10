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


@group_required('Admin', 'Information seeker')
def infoseeker(request):
    return render(request, 'accounts/infoseeker.html')

@group_required('Admin', 'Information contributor')
def infocontributor(request):
    return render(request, 'accounts/infocontributor.html')

@group_required('Admin', 'Service user')
def serviceuser(request):
    return render(request, 'accounts/serviceuser.html')

@group_required('Admin', 'Service coordinator')
def servicecoor(request):
    return render(request, 'accounts/servicecoor.html')

@group_required('Admin')
def admin_panel(request):
    return render(request, 'accounts/admin_panel.html')

@group_required('Admin', 'Service user')
def leave_application(request):
    return render(request, 'accounts/leave_application.html')

@group_required('Admin', 'Service user')
def service_request(request):
    return render(request, 'accounts/service_request.html')

@group_required('Admin', 'Service user')
def book_resource(request):
    return render(request, 'accounts/book_resource.html')