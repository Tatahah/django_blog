from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, cream, cookie, candy, cupcake!"}
    # return HttpResponse("Rango says hey there partner!<br/> <a href='/rango/about/'>About</a>")
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'ownerdata': 'Kacpi kocha Malgi'}
    # return HttpResponse("Rango says here is the about page.<br/> <a href='/rango/'>Return</a>")
    return render(request, 'rango/about.html', context=context_dict)