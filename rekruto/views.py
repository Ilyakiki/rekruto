from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'rekruto/home.html')

def rekruto(request):
    name=request.GET['name']
    message=request.GET['message']
    comment='Приятно познакомиться'
    if name=='':
        return HttpResponseRedirect('https://www.youtube.com/watch?v=eBGIQ7ZuuiU')
    if '?' in name:
        comment='В вашем имени есть знак ?. Вы случайно не друг Загадочника?'
    name+='!'
    if message !='':
        message+='!'
    return render(request,'rekruto/test_html.html',{'name':name,'message':message,'comment':comment})