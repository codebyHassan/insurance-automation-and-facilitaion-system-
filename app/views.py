from django.shortcuts import render
from django.shortcuts import HttpResponse , redirect
from django.contrib.auth import login , logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
import joblib


model = joblib.load('static/Random_forest_Regression')

# Create your views here.
def home(request):
    return render(request , 'index.html' )


def blog(request):
    return render(request , 'blog.html')

def contact(request):      
    return render(request , 'contact.html')

def service(request):
    return render(request , 'service.html')


def about(request):
    return render(request , 'about.html')


def faqs(request):
    return render(request , 'FAQ.html')


def preiume(request):
    if request.method == 'POST':
        age  =  request.POST['age']
        sex  = request.POST['sex']
        bmi = request.POST['bmi']
        region = request.POST['area']
        childern = request.POST['childern']
        smoker = request.POST['smoker']

        print(age , sex, bmi , region , childern , smoker )

        # pred = round(model.predict([[age, sex, bmi , childern , smoker , region]])[0])

        pre = round (model.predict ([[age , sex , bmi , childern , smoker , region]])[0])
        context = {

            'pre':pre 
        }
        return render(request , 'preiume.html', context)
    else:
        return render(request , 'preiume.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        user = authenticate(request, username = username , password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
            
        
        else:
            return redirect('login')
    return render(request , 'login.html')


def register_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        passw = request.POST['password']


        print(uname , email , passw)

        user = User.objects.create_user(uname, email , passw)
        user.save()
        return redirect('login')
    return render(request , 'signup.html')


def logout_view(request):
    logout(request)
    return redirect('login')
