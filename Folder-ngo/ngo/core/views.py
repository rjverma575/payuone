from django.shortcuts import render

# Create your views here.
def index (request):
    context = {'indexActive' : 'active'}
    return render(request, 'core/index.html', context)
