from django.shortcuts import render

# Create your views here.
def hyderabad(request):
    return render(request,'hyderabad.html')
def mumbai(request):
    return render(request,'mumbai.html')