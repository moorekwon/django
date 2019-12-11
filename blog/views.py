import os
from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    # 상위 폴더(blog)의
    # 상위 폴더(djangogirls)의
    # 하위폴더(templates)의
    # 하위파일(post_list.html)
    # 내용을 read()한 결과를 HttpResponse에 인자로 전달

    # 경로 이동
    # os.path.abspath(__file__) <- 현재 파일의 절대 경로를 리턴해줌
    # os.path.dirname
    # os.path.join

    # 파일 열기
    # open
    cur_file_path = os.path.abspath(__file__)
    blog_dir_path = os.path.dirname(cur_file_path)
    root_dir_path = os.path.dirname(blog_dir_path)
    templates_dir_path = os.path.join(root_dir_path, 'templates')
    post_list_html_path = os.path.join(templates_dir_path, 'post_list.html')

    # print(cur_file_path)
    # print(blog_dir_path)

    print(templates_dir_path)
    # /home/hyojinkwon/projects/wps12th/djangogirls/templates

    f = open(post_list_html_path, 'rt')
    html = f.read()
    f.close()

    return HttpResponse(html)
