"""
    qa/models.py
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    """
    Question Manager
    """
    def new(self):
        """ new func """
        return self.order_by('-id')
    def popular(self):
        """ popular func """
        return self.order_by('-rating')


class Question(models.Model):
    """
    Question - вопрос
        title - заголовок вопроса
        text - полный текст вопроса
        added_at - дата добавления вопроса
        rating - рейтинг вопроса (число)
        author - автор вопроса
        likes - список пользователей, поставивших "лайк"
    """
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="question_like_user")
    def __str__(self):
        return str(self.title)



class Answer(models.Model):
    """
    Answer - ответ
        text - текст ответа
        added_at - дата добавления ответа
        question - вопрос, к которому относится ответ
        author - автор ответа
    """
    objects = models.Manager()
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.text)
