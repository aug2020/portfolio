from django.shortcuts import render
from .models import Project
# Create your views here.
def homepage(request):
    projects = Project.objects.all() # this grabs all the project objects
    return render(request,'portfolio/home.html',{'projects': projects})