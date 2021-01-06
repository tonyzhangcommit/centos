from django.shortcuts import render
import time
# Create your views here.
from django.http import JsonResponse


def createUser(request):
    print('测试新的请求函数')
    return JsonResponse({'msg':'success'})