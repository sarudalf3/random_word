from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if 'count' in request.session:
        request.session['count'] +=  1
    else:
        request.session['count'] = 1
    
    request.session['value'] = get_random_string(length=32)    
    return render(request, 'random_word/index.html')


def reset(request):
    request.session['count'] = 1
    return redirect('random_word/index.html')
