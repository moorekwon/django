from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>Post List!</h1>'
        '<div>'
        '<p>published: 12.11.2019, 14.:38</p>'
        '<h2><a href="">My First post</a></h2>'
        '<p>Hello</p>'
        '</div>'
        '<p>published: 12.11.2019, 14.:39</p>'
        '<h2><a href="">My Second post</a></h2>'
        '<p>Hi</p>'
        '</div>'
        '</body>'
        '</html>'
    )
