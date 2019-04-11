from django.shortcuts import render,redirect
from .models import User
# Create your views here.
from . import form


def index(request):

    return render(request,'index.html')


def login(request):
    if request.session.get('is_login',None):

        return redirect("/index/")
    if request.method == 'POST':
        login_form = form.UserForm(request.POST)
        message = '请填写所有字段'
        if login_form.is_valid():
            print(login_form)
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)

                if password == user.password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['username'] = user.name
                    return redirect('/index/')
                else:
                    message = '密码错误'
            except:
                message = '用户不存在'
    login_form = form.UserForm()
    return render(request,'login/login.html',locals())


def register(request):
    if request.session.get('is_login', None):

        return redirect('/index/')
    message = '清检查拼写内容'
    register_form = form.RegisterForm(request.POST)
    print(register_form.is_valid())
    if register_form.is_valid():
        print('有数据')
        #获取数据
        username = register_form.cleaned_data['name']
        password1 = register_form.cleaned_data['password1']
        password2 = register_form.cleaned_data['password2']
        email = register_form.cleaned_data['email']
        sex = register_form.cleaned_data['sex']
        if password1 != password2:
            message = '两次输入的密码不相同'
            print('密吗',password1,password2)
        else:
            same_name_user = User.objects.filter(name=username)
            if same_name_user:
                message = '用户已存在'
            else:
                user_save = User()
                user_save.name = username
                user_save.password = password2
                user_save.email = email
                user_save.sex = sex
                user_save.save()
                print('保存')
                return redirect('/login/')
    register_form = form.RegisterForm()
    return render(request,'login/register.html',locals())


def logout(request):
    if not request.session.get('is_login',None):
        #说明没有登陆
        return redirect('/index/')
    #清除会话
    request.session.flush()
    return redirect("/index")

