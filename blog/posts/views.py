from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.http import JsonResponse

# Create your views here.

def health(request):
    return HttpResponse("Health is Ok")

def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request,'index.html',{'posts':posts})

def add_blog(request):
    if request.method == 'POST':
        Post(title=request.POST.get('title'),content=request.POST.get('content')).save()
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


