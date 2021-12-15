from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request,'customer/home.html')

def RegisterPage(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
    context = {'form':form}
    return render(request, 'user/register.html',context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/adminhome')
    return render(request,'user/login.html')   


def LogoutPage(request):
    logout(request)
    return redirect('/login')

