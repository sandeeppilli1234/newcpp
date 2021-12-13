from django.shortcuts import redirect, render
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate , login
from hrentalApp.models import Property , Enquiries , Registered 
from django.contrib import  messages
# Create your views here.
def login(request):
    return render(request , 'login.html')

def loggingin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']
        print(1)
        user = auth.authenticate(username = username , password = password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return render(request , 'home.html')

        else:
            messages.info(request, 'Invalid credentials')
            return redirect('loggingin')
    return render(request,'login.html')

def register(request):
    return render(request, 'register.html')

def home(request):
    prop_rent = Property.objects.filter(Status = "rent")[0]
    prop_buy = Property.objects.filter(Status = "sale")[0]
    print(prop_buy)
    print(prop_rent)
    
    context = {
        'houses_rent' : prop_rent,
        'houses_buy' : prop_buy,
    }
    return render(request, 'home.html', context)

def registeration(request):
    if request.method == "POST":
        first_name = request.POST['firstname'] 
        last_name = request.POST['lastname']

        email= request.POST['Email'] 
        username= request.POST['username'] 
        password = request.POST['pass'] 
        user = User.objects.create_user( first_name= first_name,last_name=last_name, username = username, email = email, password = password)
        print(user)
        reg = Registered( firstname= first_name,lastname=last_name, username = username, email = email, password = password)
        reg.save()
        
    return render(request,'login.html')

def buy(request):
    prop_sale = Property.objects.filter(Status = "sale")
    print(prop_sale)
    context = {
        'houses' : prop_sale,
    }
    return render(request , 'buy.html', context)

def sell(request):
    prop_rent = Property.objects.filter(Status = "rent")

    context = {
        'houses' : prop_rent,
    }
    return render(request , 'sell.html',context)

def properties(request):
    print("-------------------------------")
    houses = Property.objects.all()

    
    for i in houses:
        print(i.hoster)
    context = {
        'houses' : houses, 
    }

    for i in context:
        print(i)
    return render(request , 'properties.html' ,context)

def contact(request):
    return render(request , 'contact.html')

def create_prop(request):
    return render(request , 'create_prop.html')

def create_prop_account(request):
    
    if request.method == 'POST':
        email = request.POST['Email']
        address = request.POST['Address']
        price = request.POST['Price']
        segment = request.POST['segment']
        status = request.POST['status']
        area = request.POST['area']
        data_prop = Property(hoster = email, Name_Address = address ,segment = segment , price = price, Area = area, Status = status )
        data_prop.save()

        houses = Property.objects.all()

    
        for i in houses:
            print(i.hoster)
        context = {
            'houses' : houses, 
        }



        return render(request, 'properties.html', context )

def enquiry(request):
    if request.method =="POST":
        enquirer = request.POST['name']
        enquirer_email = request.POST['email']
        enquiry_message = request.POST['message']
        
        enq = Enquiries(enquirer_name = enquirer, enquirer_email = enquirer_email, enquiry_msg = enquiry_message )
        enq.save()

        return render(request , 'contact.html')