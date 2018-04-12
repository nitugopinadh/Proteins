from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context_dict = {'boldmessage': "I am bold font from the context"}
    # return HttpResponse("Welcome to protein's world!")
	return render(request, 'Proteins/index.html', context_dict)
