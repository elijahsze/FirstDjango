from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 编写第一个视图函数，http协议

def index(request):
    return HttpResponse("图书管理系统")