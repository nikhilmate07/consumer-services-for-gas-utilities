from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from models import ServiceRequest, SupportTicket
from forms import ServiceRequestForm, SupportTicketForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'track_requests.html', {'requests': requests})

@login_required
def manage_tickets(request):
    if request.user.is_staff:
        tickets = SupportTicket.objects.all()
    else:
        tickets = SupportTicket.objects.filter(service_request__customer=request.user)
    return render(request, 'manage_tickets.html', {'tickets': tickets})
