from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Post


# Create your views here.

def health(request):
    return HttpResponse("Health is Ok")

def home(request):
    is_logedin = True
    if 'user_id' not in request.COOKIES:
        is_logedin = False
        return redirect('login')
    posts = Post.objects(user_id=request.COOKIES.get('user_id','1')).order_by('-created_at')
    return render(request,'index.html',{'posts':posts,'is_logedin':is_logedin})

def add_blog(request):
    if request.method == 'POST':
        
        Post(user_id=request.COOKIES.get('user_id','1'),title=request.POST.get('title'),content=request.POST.get('content')).save()
    return redirect('home') 

def delete_blog(request, id):
    if request.method == "POST":
        Post.objects(id=id).delete()
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failed'})

def edit_blog(request,id):
    if request.method == "POST":
        Post.objects(id=id).update(
            title=request.POST.get('title'),
            content=request.POST.get('content')
        )
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failed'})


