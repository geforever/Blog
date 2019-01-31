from django.shortcuts import render, HttpResponse, redirect
from .models import Module, Topic
from userprofile.models import Profile
from comment.models import BBS_Comment
from BBS.BBS_index.models import Module
import markdown
# Create your views here.


def BBS_index(request):
    modules = Module.objects.all()
    return render(request, 'bbs_index.html', {'modules': modules})


def BBS_topic(request, module_id):
    module = Module.objects.get(id=module_id)
    topics = Topic.objects.filter(tID_id=module_id)
    return render(request, 'BBS_topic.html', {'topics': topics, 'module': module})


def BBS_topic_detail(request, module_id, topic_id):
    if request.method == 'POST':
        Tbody = request.POST.get('Tbody')
        if request.session.get('is_login', None):
            user_id = request.session['user_id']
            if Tbody.strip():
                bbs_comment = BBS_Comment.objects.create(
                    BBScomment_content=Tbody,
                    BBScomment_ID_id=topic_id,
                    BBScomment_user_id_id=user_id
                )
                bbs_comment.save()
                return redirect('/BBS_index/module_' + str(module_id) + '/topic_' + str(topic_id) + '/')
            else:
                return redirect('/BBS_index/module_' + str(module_id) + '/topic_' + str(topic_id) + '/')
        else:
            return HttpResponse("尚未登录！！！")
    if request.method == 'GET':
        module = Module.objects.get(id=module_id)
        topic_detail = Topic.objects.get(id=topic_id)
        topic_detail.tBody = markdown.markdown(topic_detail.tBody,
                                               extensions=[
                                                   'markdown.extensions.extra',
                                                   'markdown.extensions.codehilite',
                                               ])
        user_id = topic_detail.tUser_id
        topic_user_profile = Profile.objects.get(user_id=user_id)
        bbs_comment_profile = Profile.objects.all()
        bbs_comments = BBS_Comment.objects.filter(BBScomment_ID=topic_detail.id)
        for bbs_comment in bbs_comments:
            bbs_comment.BBScomment_content = markdown.markdown(bbs_comment.BBScomment_content,
                                                               extensions=[
                                                                   'markdown.extensions.extra',
                                                                   'markdown.extensions.codehilite',
                                                               ])
        return render(request,
                      'BBS_topic_detail.html',
                      {
                          'topic_detail': topic_detail,
                          'module': module,
                          'topic_user_profile': topic_user_profile,
                          'bbs_comment_prifile': bbs_comment_profile,
                          'bbs_comments': bbs_comments,
                      })


def reply_topic(request):
    if request.method == 'POST':
        Tbody = request.POST.get('Tbody')
        print(Tbody)
