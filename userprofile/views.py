from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .forms import ProfileForm
from .models import Profile
from login.models import User

# Create your views here.


def profile_edit(request):
    id = request.session['user_id']
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=id)
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES)
        if profileform.is_valid():
            try:
                nickname = profileform.cleaned_data['nickname']
                bio = profileform.cleaned_data['bio']
                birthday = profileform.cleaned_data['birthday']
                profile.nickname = nickname
                profile.bio = bio
                profile.birthday = birthday
                if 'avatar' in request.FILES:
                    profile.avatar = profileform.cleaned_data['avatar']
                profile.save()
                request.session['user_profile'] = profile.avatar.url
                return render(request, 'userinfo.html', locals())
            except:
                message = "上传图片有误！"
                return render(request, 'userinfo.html', locals())
    elif request.method == "GET":
        profile_form = ProfileForm
        content = {'profile_form': profile_form, 'profile': profile, 'user': user}
        return render(request, 'userinfo.html', content)

def reset_pwd(request):
    status_dict = {'status': 0, 'message': '未知错误'}
    if request.is_ajax():
        old_pwd = request.POST.get('old_pwd')
        new_pwd_1 = request.POST.get('new_pwd_1')
        new_pwd_2 = request.POST.get('new_pwd_2')
        if old_pwd:
            user_id = request.session.get('user_id')
            user = User.objects.get(id=user_id)
            user_pwd = user.password
            if user_pwd == old_pwd:
                if new_pwd_1 and new_pwd_2:
                    if '' in new_pwd_2:
                        status_dict['status'] = -1
                        status_dict['message'] = "密码中不能有空字符！！！"
                        return JsonResponse(status_dict)
                    else:
                        if new_pwd_1 == new_pwd_2:
                            user.password = new_pwd_2
                            user.save()
                            status_dict['status'] = 1
                            status_dict['message'] = "修改成功!"
                            return JsonResponse(status_dict)
                        else:
                            status_dict['status'] = -1
                            status_dict['message'] = "两次输入密码不一致，请重新输入！！！"
                            return JsonResponse(status_dict)
                else:
                    status_dict['status'] = -1
                    status_dict['message'] = "密码不能为空"
                    return JsonResponse(status_dict)
            else:
                status_dict['status'] = -1
                status_dict['message'] = "密码输入错误，请重新输入"
                return JsonResponse(status_dict)
        else:
            status_dict['status'] = -1
            status_dict['message'] = "初始密码不能为空！！！"
            return JsonResponse(status_dict)
        #return HttpResponse("初始密码{},新密码{},确认密码{}".format(old_pwd, new_pwd_1, new_pwd_2))