from django.shortcuts import render

# Create your views here.
def home(request):
    name = request.GET['name']
    message = request.GET['message']
    return render(request,'rekruto/home.html',{'name': name, 'message': message})

'''def rekruto(request):
    name=request.GET['name']
    message=request.GET['message']
    return render(request,'rekruto/test_html.html',{'name':name,'message':message})'''