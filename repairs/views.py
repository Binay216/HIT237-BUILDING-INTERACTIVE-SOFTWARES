from django.shortcuts import render, redirect
from .models import RepairRequest

def home(request):
    return render(request, 'home.html')

def create_request(request):
    if request.method == 'POST':
        RepairRequest.objects.create(
            tenant=request.user,
            issue_type=request.POST.get('issue_type'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            location=request.POST.get('location'),
            priority=request.POST.get('priority'),
        )
        return redirect('home')

    return render(request, 'create_request.html')