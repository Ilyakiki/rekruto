from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'rekruto/home.html')

def rekruto(request):
    name=request.GET['name']
    message=request.GET['message']
    return render(request,'rekruto/test_html.html',{'name':name,'message':message})