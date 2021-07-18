from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm
from .models import Dsuser
from django.contrib.auth.hashers import make_password
from .forms import LoginForm

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        dsuser = Dsuser(
            id=form.data.get('id'),
            email=form.data.get('email'),
            password=make_password(form.data.get('password'))
        )
        dsuser.save()

        self.request.session['user'] = form.data.get('id')

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('id')

        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')

def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/user/login')
        return function(request, *args, **kwargs)

    return wrap

