from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import VerifyCode
from django.conf import settings
from django.core.mail import send_mail
from .forms import VerifyCodeForm
# Create your views here.

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = "user_app/register.html"
    success_url = reverse_lazy("confirm_code")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        
        verify_code = VerifyCode.objects.create(code = 0, user = user)
        verify_code.generate_code()
        
        send_mail(
            subject="Verify code", 
            message=f"Your code: {verify_code.code}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["worldit_academy@worldit.academy"],
            fail_silently=True
        )
        
        return redirect(self.success_url)

class CustomLoginView(LoginView):
    template_name = "user_app/login.html"
    
class MainView(TemplateView):
    template_name = "user_app/main.html"
    
class ConfirmCodeView(FormView):
    template_name = "user_app/verificate.html"
    form_class = VerifyCodeForm
    success_url = reverse_lazy("login")

    def form_valid(self, form: VerifyCodeForm):
        code = form.cleaned_data.get("code")
        verify_code = VerifyCode.objects.filter(code = code).first()
        print(code, verify_code)
        
        if verify_code and verify_code.is_valid():
            verify_code.user.is_active = True
            verify_code.user.save()
            return redirect(self.success_url)
        else:
            form.add_error("code", "Такого коду не існує, або його час вичерапно.")
            return self.form_invalid(form)
    
# Під час валідації форми у views щоб додати помилку:
# form.add_error("поле", "текст")
# Та щоб повернути форму з помилкою -> return self.form_invalid(form)