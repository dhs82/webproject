from django.shortcuts import render

# Create your views here.

def bookmark(request):
    return render(request, 'main/bookmark.html')

def info(request):
    return render(request, 'main/info.html')

def recommend(request):
    return render(request, 'main/recommend.html')

def homelands(request):
    return render(request, 'main/homelands.html')

def test(request):
    return render(request, 'main/test.html')
