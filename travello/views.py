from django.shortcuts import render
from .models import Destination
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests' : dests})
