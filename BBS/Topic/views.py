from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from BBS.BBS_index.models import Topic
from BBS.BBS_index.models import Module
from login.models import User
# Create your views here.


def addTopic(request):
    message = ''
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.method == 'POST':
        if request.POST.get('topic_title').strip():
            if request.POST.get('topic_body').strip():
                try:
                    user = User.objects.get(id=request.session['user_id'])
                except:
                    message = '用户名不存在'
                    return HttpResponse(message)
                topic_title = request.POST.get('topic_title')
                topic_body = request.POST.get('topic_body')
                module_select = request.POST.get('model_select')
                module_id = Module.objects.get(id=module_select).id
                topic = Topic.objects.create(
                    tID_id=module_id,
                    tUser_id=user.id,
                    tTitle=topic_title,
                    tBody=topic_body
                )
                topic.save()
                return redirect('/BBS_index/module_' + str(module_id) + '/')
            else:
                message = "内容不能为空！"
                return render(request, 'addTopic.html', {'message': message})
        else:
            message = "标题不能为空！"
            return render(request, 'addTopic.html', {'message': message})
    if request.method == 'GET':
        modules = Module.objects.all()
        return render(request, 'addTopic.html', {'modules': modules})