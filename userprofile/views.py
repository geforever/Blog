from django.shortcuts import render, HttpResponse
from .forms import ProfileForm
from .models import Profile
from login.models import User

# Create your views here.


def profile_edit(request):
    id = request.session['user_id']
    print("用户ID为：",id)
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id=id)
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES)
        if profileform.is_valid():
            try:
                print("显示用户昵称：", profileform.cleaned_data['nickname'])
                nickname = profileform.cleaned_data['nickname']
                bio = profileform.cleaned_data['bio']
                birthday = profileform.cleaned_data['birthday']
                profile.nickname = nickname
                profile.bio = bio
                profile.birthday = birthday
                if 'avatar' in request.FILES:
                    profile.avatar = profileform.cleaned_data['avatar']
                profile.save()
                return render(request, 'userinfo.html', locals())
            except:
                message = "上传图片有误！"
                return render(request, 'userinfo.html', locals())
    elif request.method == "GET":
        profile_form = ProfileForm
        content = {'profile_form': profile_form, 'profile': profile, 'user': user}
        return render(request, 'userinfo.html', content)

