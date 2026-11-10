from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordMixin, AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Електронна пошта",
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"})
    )
    password1, password2 = SetPasswordMixin.create_password_fields("Пароль", "Підтверди пароль")

    class Meta:
        model = User
        fields = ['email']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Електронна пошта",
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"})
    )  

class VerifyCodeForm(forms.Form):
    code = forms.CharField(
        max_length=6,
        required=True,
        widget=forms.TextInput(),
        label="Код підтвердження"
    )

class FirstEntryForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'pseudonym']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError("Введіть ім'я користувача")
        username = username.strip()

        if User.objects.filter(username__iexact = username).exists():
           raise forms.ValidationError("Користувач з таким ім'ям вже існує")  

        return username

    def clean_pseudonym(self):
        pseudonym = self.cleaned_data.get('pseudonym')
        if pseudonym and pseudonym.strip() and User.objects.filter(pseudonym__iexact = pseudonym.strip()).exists():
            raise forms.ValidationError("Користувач з таким псевдонімом вже існує")  

        return pseudonym

        # __iexact в Модель.objects.filter(поле__iexact=значення) - щоб не враховувати регістер літер