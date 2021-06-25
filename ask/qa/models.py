"""
    qa/models.py
"""
from django import db
from django import contrib


class QuestionManager(db.models.Manager):
    """
    Question Manager
    """
    def new(self):
        """ new func """
        return self.order_by('-id')
    def popular(self):
        """ popular func """
        return self.order_by('-rating')


class Question(db.models.Model):
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
    title = db.models.CharField(max_length=255)
    text = db.models.TextField()
    added_at = db.models.DateTimeField(auto_now_add=True)
    rating = db.models.IntegerField(default=0)
    author = db.models.ForeignKey(contrib.auth.models.User,
                                  on_delete=db.models.CASCADE,
                                  related_name="question")
    likes = db.models.ManyToManyField(contrib.auth.models.User, default=None,
                                      related_name="question_like_user")

    class Meta:
        ordering = ["-added_at"]

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return "/question/{:d}/".format(self.pk)


class Answer(db.models.Model):
    """
    Answer - ответ
        text - текст ответа
        added_at - дата добавления ответа
        question - вопрос, к которому относится ответ
        author - автор ответа
    """
    objects = db.models.Manager()
    text = db.models.TextField()
    added_at = db.models.DateTimeField(auto_now_add=True)
    question = db.models.ForeignKey(Question, on_delete=db.models.CASCADE,
                                    related_name="answer")
    author = db.models.ForeignKey(contrib.auth.models.User,
                                  on_delete=db.models.CASCADE,
                                  related_name="answer")

    class Meta:
        ordering = ["-added_at"]

    def __str__(self):
        return str(self.text)
