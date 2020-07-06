from django.shortcuts import render,HttpResponse,redirect
from priceprediction.models import Contact,Password
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    if(request.user.is_anonymous):
        return redirect("/login")
    else:
        return render(request,'priceprediction/index.html')
def about(request):
    if(request.user.is_anonymous):
        return redirect("/login")
    return render(request,'priceprediction/about.html')

def services(request):
    if(request.user.is_anonymous):
        return redirect("/login")
    return render(request,'priceprediction/services.html')
def contact(request):
    if(request.user.is_anonymous):
        return redirect("/login")
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        textarea=request.POST.get('textarea')
        contact=Contact(name=name,email=email,phone=phone,textarea=textarea)
        contact.save()
        messages.success(request,'your message has been sent')
    return render(request,'priceprediction/contact.html')
def logindevta(request):
    if(request.method=="POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')
        z=Password(username=username,password=password)
        z.save()
        user=authenticate(username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect("/")
        else:
            return render(request,'priceprediction/login.html')
    return render(request,'priceprediction/login.html')
def logoutdevta(request):
    logout(request)
    return redirect("/login/")
def register(request):
    if(request.method == "GET"):
        form=UserCreationForm(request.GET)
        if(form.is_valid()):
            form.save()
            return redirect('/login/')
        else:
            form=UserCreationForm()
    return render(request,'priceprediction/register.html',{'form':form})
