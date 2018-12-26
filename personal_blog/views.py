from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from personal_blog.models import Blog
from login.models import User
from uservideo.models import Uservideo
from .forms import AddBlogForm
import datetime
import os


# Create your views here.



def blog(request):
    a = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': a})


def my_blog(request):
    user_name = request.session.get('user_name')
    user = User.objects.get(user_name=user_name)
    my_blog = Blog.objects.filter(author_id=user.id)
    if my_blog:
        return render(request, 'my_blog.html', {'my_blogs': my_blog})
    return render(request, 'my_blog.html')


def add_blog(request):
    try:
        user_name = request.session.get('user_name')
        user = User.objects.get(user_name=user_name)
    except:
        message = "无此用户！"
        return render(request, 'my_blog.html', locals())
    if request.is_ajax():
        if request.FILES.get('video'):
            '''如果有视频，就先上传视频保存，并返回视频ID给ajax'''
            video_file = request.FILES.get('video')
            video_name = request.FILES.get('video').name
            if str(os.path.splitext(video_name)[1]).lower() != '.mp4':  # 判断是否是mp4格式文件
                message = "该文件不是MP4格式，请重新选择！"
                return render(request, 'add_blog.html', locals())
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间
            video_name = user.user_name + "-" \
                         + str(user.id) + "-" + str(now_time) + "-" + video_name
            file_second_path = str(user.user_name)
            if os.path.exists('media/video/' + file_second_path):  # 判断是否有名称为用户名字的子目录，没有就创建
                file_path = os.path.join('media/video', file_second_path, video_name)
            else:
                os.mkdir('media/video/' + file_second_path)
                file_path = os.path.join('media/video', file_second_path, video_name)
            with open(file_path, 'wb') as f:
                for chunk in video_file.chunks():  # 储存视频
                    f.write(chunk)
                f.close()
            create_video = Uservideo.objects.create(
                video_name=video_name, video_path=file_path,video_owner_id_id=user.id
            )
            create_video.save()
            title = request.POST.get('title')
            body = request.POST.get('body')
            video_id = Uservideo.objects.get(video_path=file_path).id
            video_dict = {'video_id': video_id, 'title': title, 'body': body}
            return JsonResponse(video_dict)
        if not request.POST.get('video_id'):
            '''如果没有视频上传'''
            title = request.POST.get('title')
            body = request.POST.get('body')
            if title:
                new_blog = Blog.objects.create(
                    blog_title=title, blog_body=body, author_id=user.id, blog_video_id=None
                )
                new_blog.save()  # 成功，写入数据库
                status_dict = {'status': 1, 'content': '新增成功'}
                return JsonResponse(status_dict)
            else:
                status_dict = {'status': 0, 'content':'新增失败，标题不能为空！'}
                return JsonResponse(status_dict)
        video_id = request.POST.get('video_id')
        if request.POST.get('title'):
            title = request.POST.get('title')
            body = request.POST.get('body')
            new_blog = Blog.objects.create(
                blog_title=title, blog_body=body, author_id=user.id, blog_video_id=video_id
            )
            new_blog.save()
            status_dict = {'status': 1 ,'content': '新增成功'}
            return JsonResponse(status_dict)
        status_dict = {'status': 0, 'content': '新增失败，标题不能为空！'}
        return JsonResponse(status_dict)
    return render(request, 'add_blog.html')


def article_detail(request, id):
    id = int(id)
    article_detail = Blog.objects.get(id=id)
    if article_detail.blog_video_id:
        uservideo = Uservideo.objects.get(id=article_detail.blog_video_id)
        return render(request, 'detail.html', {'article_detail': article_detail, 'uservideo': uservideo})
    else:
        return render(request, 'detail.html', {'article_detail': article_detail})