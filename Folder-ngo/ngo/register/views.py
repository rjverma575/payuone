from django.shortcuts import render, redirect
from .models import UserRegister
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    context = {'registerActive' : 'active'}
    if request.method == 'POST':
        nm = request.POST['name']
        em = request.POST['email']
        ph = request.POST['phone']
        msg = request.POST['message']


        #validations
        error_message = None
        values = {
            'FilledName' : nm,
            'FilledEmail' : em,
            'FilledPhone' : ph,
            'Filledmsg' : msg
        }

        if(not nm):
            error_message = "Name is required !!"
        elif not em:
            error_message = "Email is required !!"
        elif not ph:
            error_message = "Phone is required !!"
        elif len(ph) < 10:
            error_message = "Phone must be 10 char long !!"
        elif not msg:
            error_message = "Message is required !!"

        #validations
        if not error_message:
            reg = UserRegister(name=nm, email=em, phone=ph, message=msg)
            reg.save()
            return render(request, 'register/register.html', context)
        else:
            data = {
                'error': error_message,
                'value' : values,
                'registerActive' : 'active'
            }
            #return redirect('register')
            return render(request, 'register/register.html', data)
    else:
        return render(request, 'register/register.html', context)
