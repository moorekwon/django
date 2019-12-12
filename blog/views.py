from django.shortcuts import render
from blog.models import Post

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
    # cur_file_path = os.path.abspath(__file__)
    # blog_dir_path = os.path.dirname(cur_file_path)
    # root_dir_path = os.path.dirname(blog_dir_path)
    # templates_dir_path = os.path.join(root_dir_path, 'templates')
    # post_list_html_path = os.path.join(templates_dir_path, 'post_list.html')
    #
    # # print(cur_file_path)
    # # print(blog_dir_path)
    #
    # print(templates_dir_path)
    # # /home/hyojinkwon/projects/wps12th/djangogirls/templates
    #
    # f = open(post_list_html_path, 'rt')
    # html = f.read()
    # f.close()
    #
    # return HttpResponse(html)


    # posts라는 변수에 전체 Post를 갖는 QuerySet 객체를 전달
    # Post.objects.무언가...를 실행한 결과는 QuerySet 객체가 됨
    # context라는 dict를 생성하며 'posts' 키에 위 posts 변수를 value로 사용하도록 함
    # render의 3번째 위치인자로 위 context 변수를 전달
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    # Template을 찾을 경로에서 post_list.html을 찾아 text로 만들고 HttpResponse 형태로 돌려줌
    # shortcut 함수
    return render(request, 'post_list.html', context)


def post_detail(request):
    # URL: /post-detail/
    # View: post_detail
    # Template: post_detail.html

    # 전체 Post 목록(Post 전체 QuerySet) 중 [0] index에 해당하는 Post 객체 하나를 post 변수에 할당
    # 'context'라는 이름의 dict를 만들어 'post' key 위에 위 post 변수를 value로 사용
    # 이 context 변수를 render의 3번째 인자로 전달
    # post_detail.html에서는 전달받은 'post' 변수의 title, author, text, created_date, published_date를 출력
    post = Post.objects.all()[0]
    context = {
        'post': post
    }


    return render(request, 'post_detail.html', context)