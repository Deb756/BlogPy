from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse,JsonResponse
from .models import Users
import json
from mongoengine import NotUniqueError

# Create your views here.
def get_users(request):
    return HttpResponse("Users data")

from django.shortcuts import render, redirect
from .models import Users # Ensure you import your model

def register(request):
        if request.method == 'POST':
            try:
            # 1. Save the user
                Users(
                    uname=request.POST.get('uname'),
                    email=request.POST.get('email'),
                    password=make_password(request.POST.get('password'))
                ).save()
                
                # 2. Redirect to login ONLY after saving
                return render(request, 'login.html' ,{'success':"Successfully Registered Login to continue"})
            except NotUniqueError:
            # This catches the "Email already exists" error
                return render(request, 'error.html', {'error': "An account with this email already exists. Please try a different email or login."})

            except Exception as e:
                # This is a "catch-all" for any other unexpected errors
                return render(request, 'error.html', {'error': f"A database error occurred: {str(e)}"})

        # 3. If it's a GET request, show the registration form
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        user = Users.objects(uname=request.POST.get('uname')).first()
        passw = check_password(request.POST.get('password'),user.password)
        if user and passw:
            request.session['user_id'] = str(user.id)
            request.session['username'] = user.uname
            return redirect('home')
        else:
             return render(request, 'login.html',{'error':'Invalid Credential'})
    return render(request, 'login.html')

def logout(request):
          request.session.flush() # Deletes session data and the cookie
          return redirect('login')


# def login(request):
#     if request.method == 'POST':
#         # 1. Fetch user by username
#         user = Users.objects(uname=request.POST.get('uname')).first()
        
#         # 2. Validate password (Note: Plain text check as requested)
#         if user and user.password == request.POST.get('password'):
#             # 3. Store string versions of data in session
#             request.session['user_id'] = str(user.id) 
#             request.session['user_name'] = user.uname
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid Credentials'})
        
#     return render(request, 'login.html')