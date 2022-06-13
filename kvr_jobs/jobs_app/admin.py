from django.contrib import admin
from jobs_app.models import HydJobs,BangaloreJobs,MumbaiJobs
# Register your models here.

class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company' ,'position','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)

class BangaloreJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company' ,'position','eligibility','address','email','phonenumber']
admin.site.register(BangaloreJobs,BangaloreJobsAdmin)

class MumbaiJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company' ,'position','eligibility','address','email','phonenumber']
admin.site.register(MumbaiJobs,MumbaiJobsAdmin)