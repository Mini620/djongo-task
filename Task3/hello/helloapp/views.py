from django.shortcuts import render
from django.http import HttpResponse

def Hello(request):
    return HttpResponse("Hello, Django!")
    
    
    
    
    #return render(request, 'helloapp/hello.html')