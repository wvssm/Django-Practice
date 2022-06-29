from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.") #뷰 생성하기
    #클라이언트에게 전달