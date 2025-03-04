from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) : 
    return render(request,'index.html')
def coffee(request) : 
    return render(request,'coffee/coffee.html')
def slogan(request) :
   return HttpResponse('''在忙也要隌你喝杯咖啡!!<br>
                        <a href='/coffee'>Coffee</a><br>
                         <a href='/'>Home</a>
                        ''')                 