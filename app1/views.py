from django.shortcuts import render, redirect
from .forms import complaintsform, passornot, princord
from .models import complaints
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
user = None
comps = complaints.objects.all()
access1 = {'access':False,
        'comps':comps,
        'decision':passornot()}
access2 = {'access':False,
        'comps':comps,
        'decision':princord()}

def home(request):
    complaints.objects.filter(rejected1=True).delete()
    complaints.objects.filter(acceptable=False).delete()
    if request.method == 'POST':
        auth.logout(request)
        redirect('/')
    total_comps = complaints.objects.count()

    context={'tot':total_comps,
            
            }
    return render(request,'home.html',context)

def add_comp(request):
    form = complaintsform()
    if request.method == 'POST':
        form = complaintsform(request.POST)
        print(request.POST)
        print(request.user)
        if form.is_valid():
            if request.POST['anonyomous'] == 'false':
                complaints.objects.create(complainer=request.user, actual=request.POST.get('actual'),anonyomous=False,about=request.POST['about'])
            else:
                complaints.objects.create(complainer=request.user, actual=request.POST.get('actual'),anonyomous=True,about=request.POST['about'])
            return redirect('home')
    context={'form':form}
    return render(request,'add_comp.html',context)

def auth1(request):

    if request.method == 'POST':
        if request.POST['code'] == 'EGS@1234' and request.POST['username'] == 'sc123':
            access1['access'] = True
            access1['comps'] = complaints.objects.all()
            access1['decision'] = passornot()
            return redirect('sd')
        else:
            return render(request,'auth1.html',{'incor':'invalid please try again'})
    else:
        return render(request,'auth1.html',{'incor':''})

def auth2(request):
    if request.method == 'POST':
        if request.POST['code'] == 'EGS@1234!' and request.POST['username'] == 'p/c#123':
            access2['access'] = True
            access2['comps'] = complaints.objects.all()
            access2['decision'] = princord()
            return redirect('pc')
        else:
            return render(request,'auth2.html',{'incor':'invalid please try again'})
    else:
        return render(request,'auth2.html',{'incor':''})


def sd(request):
    access1['decision'] = passornot()
    if request.method == 'POST':
        complaint = complaints.objects.get(id=request.POST['id'])
        updated = passornot(request.POST,instance=complaint)
        updated.save()
        access1['access'] = True
        access1['comps'] = complaints.objects.all()
        access1['decision'] = passornot()
        return render(request,'sd.html',access1)
    return render(request,'sd.html',access1)

def pc(request):
    access2['decision'] = princord()
    if request.method == 'POST':
        complaint = complaints.objects.get(id=request.POST['id'])
        decided = princord(request.POST,instance=complaint)
        decided.save()
        access2['access'] = True
        access2['comps'] = complaints.objects.all()
        access2['decision'] = princord()
        return render(request,'pc.html',access2)
    return render(request,'pc.html',access2)

def register_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        rpassword = request.POST['rpassword']

        if rpassword == password:
            if User.objects.filter(username= username).exists():
                messages.info(request,'Username already used')
                return redirect('register')
            else:
                user = User.objects.create(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('register')

    return render(request,'registration.html')

def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'credentials invalid')
            return redirect('login')

    return render(request,'login.html')
def fix(request):
    return redirect('login')
def fix2(request):
    return redirect('register')
