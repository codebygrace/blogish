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