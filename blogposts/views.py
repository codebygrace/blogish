from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blogposts/template.html')

def post(request):
    return render(request, 'blogposts/post.html')