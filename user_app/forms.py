from django import forms

class VerifyCodeForm(forms.Form):
    code = forms.CharField(
        max_length=6,
        required=True,
        widget=forms.TextInput(),
        label="Код підтвердження"
    )

