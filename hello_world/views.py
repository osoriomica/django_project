from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Handle form submission
        return HttpResponse(f"You must have POSTed something.")
    else:
        return HttpResponse(request.method)