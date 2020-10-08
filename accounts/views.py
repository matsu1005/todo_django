from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy


class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/login.html'


# class SignUp(CreateView):
#     form_class = SignUpForm
#     template_name = "accounts/signup.html" 
#     success_url = reverse_lazy('todo:index')

#     def form_valid(self, form):
#         user = form.save() # formの情報を保存
#         login(self.request, user) # 認証
#         self.object = user 
#         return HttpResponseRedirect(self.get_success_url()) # リダイレクト

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('todo:index'))
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})