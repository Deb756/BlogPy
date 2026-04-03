from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Users
import json

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
                    password=request.POST.get('password')
                ).save()
                
                # 2. Redirect to login ONLY after saving
                return render(request, 'login.html' ,{'success':"Successfully Registered Login to continue"})
            except json.JSONDecodeError:
                 return JsonResponse({"error": "Invalid JSON"}, status=400)

        # 3. If it's a GET request, show the registration form
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        user = Users.objects(uname=request.POST.get('uname'), password=request.POST.get('password')).first()
        if user:
            response = redirect('home')
            # Set a cookie with the user ID
            response.set_cookie('user_id', str(user.id))
            return response
        else:
             return render(request, 'login.html',{'error':'Invalid Credential'})
    return render(request, 'login.html')

def logout(request):
     if request.method == 'POST':
          response = JsonResponse({'status':'success'})
          response.delete_cookie('user_id')
          return response


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