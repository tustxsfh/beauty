import imp
from django.shortcuts import render
from django.shortcuts import redirect
import random

def url_random(): 
    k = random.randint(1,5)
    url1 = 'https://i.tuiimg.net/00' + str(k) + '/'
    url3 = '.jpg'
    i = random.randint((k-1)*500+1, 500*k)
    j = random.randint(1, 40)
    url_1 = url1 + str(i) + '/' + str(j) + url3
    return url_1


def girl_random(request):
    url_girl = url_random()
    print(url_girl)
    context = {'url_girl':url_girl}
    print(context)
    return render(request, 'index.html',context)
