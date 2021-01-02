from django.shortcuts import render,request

# Create your views here.
def homepage(request):
    return render(request, 'blog/home.html', {})