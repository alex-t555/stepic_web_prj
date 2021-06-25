"""
    qa/forms.py
"""
from django import forms
from django import contrib

from qa.models import Question, Answer

class AskForm(forms.ModelForm):
    """
    AskForm - форма добавления вопроса
        title - поле заголовка
        text - поле текста вопроса
    """

    class Meta:
        model = Question
        fields = ("title", "text",)

    def save(self, commit=True):
        question = super().save(commit=False)
        if commit:
            question.save()
        return question


class AnswerForm(forms.ModelForm):
    """
    AnswerForm - форма добавления ответа
        text - поле текста ответа
        question - поле для связи с вопросом
    """

    class Meta:
        model = Answer
        fields = ("text",)

    def save(self, commit=True):
        answer = super().save(commit=False)
        if commit:
            answer.save()
        return answer


class SignupForm(contrib.auth.forms.UserCreationForm):
    """
    username - имя пользователя, логин
    email - email пользователя
    password - пароль пользователя
    """
    email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = contrib.auth.models.User
        fields = ("username", "email", "password1", "password2",)
        # widgets = {
        #     "password1": forms.TextInput(attrs={"name": "password"}),
        # }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password",
                                widget=forms.PasswordInput)

    class Meta:
        model = contrib.auth.models.User
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get("password") != cd.get("password2"):
            raise forms.ValidationError("Passwords don't match.")
        return cd.get("password2")
