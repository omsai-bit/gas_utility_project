# customer_service/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm # type: ignore
from .models import ServiceRequest

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

@login_required
def request_list(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customer_service/request_list.html', {'service_requests': service_requests})

# customer_service/views.py


def homepage(request):
    return render(request, 'customer_service/homepage.html')
