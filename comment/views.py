from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from login.models import User
from .models import Comment
# Create your views here.

def Comment_post(request, article_id):
    status_dict = {'status': 0, 'message': "错误"}
    if request.is_ajax():
        try:
            user_id = User.objects.get(id=request.session['user_id'])
            comment_content = request.POST.get('body')
            if comment_content:
                comment_blog_id = article_id
                comment_user_id = user_id.id
                comment = Comment.objects.create(
                    comment_content=comment_content,
                    comment_blog_id_id=comment_blog_id,
                    comment_user_id_id=comment_user_id,
                )
                comment.save()
                status_dict['status'] = 1
                status_dict['message'] = "提交成功"
                return JsonResponse(status_dict)
            else:
                status_dict['status'] = -1
                status_dict['message'] = "评论内容不能为空"
                return JsonResponse(status_dict)
        except:
            status_dict['status'] = -1
            status_dict['message'] = "意外错误"
            return JsonResponse(status_dict)
    else:
        return HttpResponse("发表评论仅接受POST请求。")
