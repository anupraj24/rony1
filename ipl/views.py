from django.shortcuts import render

from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

# @login_required(login_url="/account/login/")
# def home_view(request):
#     # ques = Question.objects.all()

#     return render(request,'home.html')

def home(request):
    return render(request,'home1.html')








@login_required(login_url="/account/login/")
def csk(request):
    return render(request,'csk.html')

def dc(request):
    return render(request,'dc.html')

def kkr(request):
    return render(request,'kkr.html')

def mi(request):
    return render(request,'mi.html')

def pxk(request):
    return render(request,'pxk.html')

def rcb(request):
    return render(request,'rcb.html')

def rr(request):
    return render(request,'rr.html')

def sh(request):
    return render(request,'sh.html')





