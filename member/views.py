from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Appointment
from django.http import HttpResponseRedirect
import datetime
import time
import popup_forms
# Create your views here.
def submitted(request):
    name=request.POST['name']
    email=request.POST['email']
    mobile_no=request.POST['number']
    listed=request.POST.getlist('salon')
    time=request.POST['appt']
    date=request.POST['effective-date']
    staff=request.POST['staff']
    datas=Appointment.objects.all()
    flag=0
    sum1=0
    for liste in listed:
        sum1=sum1+int(liste)
    form_time=datetime.datetime.strptime(time,'%H:%M')-datetime.datetime(1900,1,1)
    final_time=datetime.datetime.strptime(time,'%H:%M')+datetime.timedelta(minutes=sum1)
    final_time_second=final_time-datetime.datetime(1900,1,1)
    for data in datas:
        database_stime_str=data.Time.strftime("%H:%M:%S")
        database_stime=datetime.datetime.strptime(database_stime_str,'%H:%M:%S')-datetime.datetime(1900,1,1)
        database_etime_str=data.endtime.strftime("%H:%M:%S")
        database_etime=datetime.datetime.strptime(database_etime_str,'%H:%M:%S')-datetime.datetime(1900,1,1)
        a=form_time.total_seconds()-database_stime.total_seconds()
        b=form_time.total_seconds()-database_etime.total_seconds()
        x=final_time_second.total_seconds()-database_stime.total_seconds()
        y=final_time_second.total_seconds()-database_etime.total_seconds()
        print(x)
        print(y)
        if data.Date==datetime.datetime.strptime(date,'%Y-%m-%d').date() and staff==data.staff:
            if  a>0 and b<0:
                flag=1
                print(flag)
                break
            if x>0 and y<0:
                flag=1
                break
    if flag==0:
        messages.success(request, f"your appointment has been recorded")
        AddAppointment=Appointment(name=name,Email=email,Mobile_No=mobile_no,List=listed,staff=staff,Time=time,Date=date,endtime=final_time)
        AddAppointment.save()
    elif flag==1:
        messages.error(request, f"time already occupied")
    return redirect('/home')

def status1(request,pk):
    Appointment.objects.filter(pk=pk).update(selected="appointed")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def status2(request,pk):
    Appointment.objects.filter(pk=pk).update(selected="not_appointed")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def adminhome(request):
    features=(
        ("30","haircut"),
        ("90","hair color"),
        ("89","facial"),
        ("45","oil massage"),
        ("15","threading"),
        ("29","mehendi"),
        ("40","waxing"),
        ("28","nailcare"),
        ("60","makeup"),
    )
    data=Appointment.objects.all()
    context = {
        'datas':data,
        'features':features
    }
    return render(request,"admin/home.html",context)

def search(request):
    query = request.GET['effective-date']
    data = Appointment.objects.filter(Date=query)
    return render(request,"admin/home.html",{'datas':data})
