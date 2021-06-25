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

    class Meta:
        model = contrib.auth.models.User
        fields = ("username", "email", "password1", "password2",)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
