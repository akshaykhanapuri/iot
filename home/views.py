from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    if request.method == 'POST':
        if request.POST['choice'] == 'ON':
            #LED on
            return render(request,'home.html',{'key':"ON"})

        elif request.POST['choice'] == 'OFF':
            #LED off
            return render(request,'home.html',{'key':"OFF"})
    else:
        return render(request,'home.html')
