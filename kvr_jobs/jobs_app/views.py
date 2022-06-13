from django.shortcuts import render
from jobs_app.models import HydJobs,BangaloreJobs,MumbaiJobs

# Create your views here.
def Homepage_view(request):
    return render(request,'jobs_app/index.html')


def HydJobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request,'jobs_app/hydjobs.html',my_dict)

def BlrJobs_view(request):
    jobs_list = BangaloreJobs.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request,'jobs_app/blrjobs.html',my_dict)

def MumbaiJobs_view(request):
    jobs_list = MumbaiJobs.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request,'jobs_app/mumbaijobs.html',my_dict)