from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return HttpResponse('<html><body><h1>Post List!</h1></body></html>')
