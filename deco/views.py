from django.shortcuts import render,redirect
from .models import ServiceNeed
from django.contrib.auth.models import User
# Create your views here.


def customer(request):
    if request.method =='POST':
        state = request.POST.get('state')
        phone_no = request.POST.get('Phone_no')
        city = request.POST.get('city')
        service = request.POST.get('Service')
        pin= request.POST.get('pin')

        customer = ServiceNeed(state=state,Phone_no=phone_no,city=city,pin=pin,Service=service)
        customer.save()
    return render(request,'required.html')


def vehicle(request):
    return render(request, 'vehicle.html')
def music(request):
    return render(request, 'music.html')

def photographer(request):
    return render(request, 'photographer.html')
def decorator(request):
    return render(request, 'decorater.html')

def signup(request):
    if  request.method == 'POST':
        if request.POST['passworld1'] == request.POST['passworld2']:
            try:
                user =  User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':"username Has Already Created"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['passworld2'])
                return redirect('signup.html')

        else:
            return render(request , 'signup.html' ,{'error':"password dint matches "})
    else:
        return render(request, 'signup.html')