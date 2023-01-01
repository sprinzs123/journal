from django.shortcuts import render
from .models import Entry
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'dashboard.html')