from django.contrib.auth.views import LoginView as DefaultLoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, reverse, render

from .forms_auth import LoginForm

class LoginView(DefaultLoginView):
    template_name = "my_auth/login.html"
    form = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('advito:announcement'), request)
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})