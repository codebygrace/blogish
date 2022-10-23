from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    count = Post.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'blogposts/template.html', context)


def post(request):
    return render(request, 'blogposts/post.html')