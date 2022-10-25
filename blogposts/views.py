from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    count = posts.count()
    context = {
        'count': count,
        'posts': posts,
    }
    return render(request, 'blogposts/template.html', context)

def post(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'blogposts/post.html', context)

def save_post(request):
    title = request.POST.get('title')
    author = request.user
    text = request.POST.get('text')
    new_post = Post(title=title, author=author, text=text)
    new_post.save()

def new_post(request):
    if request.method == 'POST':
        save_post(request)
        return redirect('/')
    context = {
        'method': request.method
    }
    return render(request, 'blogposts/new_post.html', context)

def edit_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blogposts/edit_post.html', {'post': post})

def update_post(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.title = request.POST.get('title')
        post.author = request.user
        post.text = request.POST.get('text')
        post.save()
    return redirect('/')

def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return render(request, 'blogposts/delete_post.html')