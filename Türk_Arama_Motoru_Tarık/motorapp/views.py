from django.shortcuts import render

# Create your views here.
def Home_Page(request):
    return render(request, "content/index.html")

def New(request):
    return render(request, "content/new.html")