from django.shortcuts import render, get_object_or_404

from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request,'current/home.html',{'jobs':jobs})

def detail(request,project_id):
    project_detail = get_object_or_404(Job,pk=project_id)
    return render(request,'current/detail.html',{'project':project_detail})