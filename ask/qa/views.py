from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request, *args, **kwargs):
    """ test method """
    return HttpResponse('200 OK')
