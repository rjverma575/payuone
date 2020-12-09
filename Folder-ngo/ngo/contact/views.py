from django.shortcuts import render
from .forms import UserMessage
from .models import User

# Create your views here.
def contact(request):
    
    if request.method == 'POST':
        fm = UserMessage(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ph = fm.cleaned_data['phone']
            msg = fm.cleaned_data['message']
            reg = User(name=nm, email=em, phone=ph, message=msg)
            reg.save()
            fm = UserMessage()
    else:
        fm = UserMessage()
    return render(request, 'contact/Contact.html', {'form':fm, 'contactActive' : 'active'})


    
