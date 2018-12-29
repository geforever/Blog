from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from login.models import User
#from login.forms import UserForm
from login.forms import Captcha
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from login.forms import RegisterForm

# Create your views here.


def index(request):
    status_duct = {'status': 0, 'message': '登录异常！'}
    #if request.session.get('is_login', None):
        #return redirect('/my_blog/')
    if request.is_ajax():
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')
        captcha = request.POST.get('captcha')  # 前端的验证码
        try:
            user = User.objects.get(user_name=get_username)
            if get_password == user.password:
                id_captcha_0 = request.POST.get('id_captcha_0')  # 前端验证码图片
                get_captcha = CaptchaStore.objects.get(hashkey=id_captcha_0)#测到验证码图片对应的验证码
                if str(captcha).lower() == get_captcha.response:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.user_name
                    status_duct['status'] = 1
                    status_duct['message'] = "登录成功！"
                    return JsonResponse(status_duct)
                else:
                    status_duct['status'] = -1
                    status_duct['message'] = "验证码错误！"
                    return JsonResponse(status_duct)
            else:
                status_duct['status'] = -1
                status_duct['message'] = "密码错误！"
                return JsonResponse(status_duct)
        except:
            status_duct['status'] = -1
            status_duct['message'] = "无此用户！"
            return JsonResponse(status_duct)
    if request.method == 'GET':
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        captcha = {'hashkey': hashkey, 'image_url': image_url}
        return render(request, 'base.html', captcha)

'''
def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(user_name=username)
                if password == user.password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.user_name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'base.html', locals())#{"message": message}
    if request.method == "GET":
        login_form = UserForm()
        return render(request, 'base.html', {'login_form': login_form})
'''


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = "请检查填写内容"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "两次输入的密码不相同"
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(user_name=username)
                if same_name_user:
                    message = "用户已经存在，请重新输入"
                    return render(request, 'register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:
                    message = "该邮箱已经被注册，请使用其他邮箱"
                    return render(request, 'register.html', locals())

                new_user = User.objects.create()
                new_user.user_name = username
                new_user.password = make_password(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())




def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    #request.session.flush()
    # 或者使用下面的方法
    del request.session['is_login']
    del request.session['user_id']
    del request.session['user_name']
    return redirect("/index/")


