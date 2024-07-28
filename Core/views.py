from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'Core/auth/signup.html')

def signin(request):
    return render(request, 'Core/auth/signin.html')

def signout(request):
    pass

def profile(request):
    return render(request, 'Core/auth/profile.html')
