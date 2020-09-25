from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 创建一个视图
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
