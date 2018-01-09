from django.shortcuts import render

# Create your views here.
def DashHome(request):
    return render(request , 'index.html')
