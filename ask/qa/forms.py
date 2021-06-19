"""
    qa/forms.py
"""
from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    """
    AskForm - форма добавления вопроса
        title - поле заголовка
        text - поле текста вопроса
    """
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q


class AnswerForm(forms.Form):
    """
    AnswerForm - форма добавления ответа
        text - поле текста ответа
        question - поле для связи с вопросом
    """
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a
