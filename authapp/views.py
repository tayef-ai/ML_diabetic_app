from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView, LoginView
from .forms import ChangePasswordForm, ResetPasswordForm, PasswordSetForm, LoginForm, RegistrationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password
# Create your views here.
class MyLoginView(LoginView):
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return HttpResponseRedirect('/dashboard/')

    #     return super().dispatch(request, *args, **kwargs)
    authentication_form=LoginForm

@login_required(login_url="/login/")
def dashboardview(request):
    user = request.user
    email = user.email
    return render(request, 'registration/dashboard.html', {'user': user, 'email': email})

@method_decorator(login_required(login_url="/login/"), name='dispatch')
class ChangePView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/changepassword.html'
    form_class=ChangePasswordForm
    success_url = '/dashboard/'
    success_message = "Password updated successfully"

class ResetPasswordView(PasswordResetView):
    template_name = 'registration/resetpassword.html'
    form_class=ResetPasswordForm
    # success_url = '/dashboard/'
    # success_message = "Password updated successfully"

class PasswordSetView(PasswordResetConfirmView):
    template_name = 'registration/passwordset.html'
    form_class=PasswordSetForm
    # success_url = '/dashboard/'
    # success_message = "Password updated successfully"

def registerview(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = make_password(form.cleaned_data['password'])
            reg = User(name=un, email=em, password=pw)
            reg.save()
            messages.success(request, "Registration Completed Successfully!!! Login Again")
            return HttpResponseRedirect('/login/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})