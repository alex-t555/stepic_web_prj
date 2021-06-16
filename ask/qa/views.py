"""
    qa/views.py
"""
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, Page
from django.db.models import QuerySet

from .models import Question, Answer

# Create your views here.
def paginate(request: HttpRequest, qs: QuerySet) -> Page:
    """
    pagination method
    """
    try:
        limit = int(request.GET.get('limit', 10))
        page = int(request.GET.get('page', 1))
    except ValueError as e:
        raise Http404 from e
    if limit > 100:
        limit = 100
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages())
    return page


def test(_: HttpRequest) -> HttpResponse:
    """ test method """
    return HttpResponse('200 OK')


@require_GET
def home(request: HttpRequest) -> HttpResponse:
    """
    URL = /?page=2
    Главная страница. Список "новых" вопросов. Т.е. последний заданный вопрос -
    первый в списке. Необходимо использовать метод new менеджера
    QuestionManager. На этой странице должна работать пагинация. Номер страницы
    указывается в GET параметре page.  На страницу выводится по 10 вопросов. В
    списке вопросов должны выводится заголовки (title) вопросов и ссылки на
    страницы отдельных вопросов.
    """
    qs = Question.objects.new()
    page = paginate(request, qs)
    return render(request, "qa/base_home.html", { "page": page })


@require_GET
def popular(request: HttpRequest) -> HttpResponse:
    """
    URL = /popular/?page=3
    Cписок "популярных" вопросов. Сортировка по убыванию поля rating.
    Необходимо использовать метод popular менеджера QuestionManager. На этой
    странице должна работать пагинация. Номер страницы указывается в GET
    параметре page.  На страницу выводится по 10 вопросов. В списке вопросов
    должны выводится заголовки (title) вопросов и ссылки на страницы отдельных
    вопросов.
    """
    qs = Question.objects.popular()
    page = paginate(request, qs)
    return render(request, "qa/base_popular.html", { "page": page })


@require_GET
def question(request: HttpRequest, id_question: str) -> HttpResponse:
    """
    # URL = /question/5/
    Страница одного вопроса. На этой странице должны выводится заголовок
    (title), текст (text) вопроса и все ответы на данный вопрос, без пагинации.
    В случае неправильного id вопроса view должна возвращать 404.
    """
    q = get_object_or_404(Question, id=id_question)
    answers = Answer.objects.filter(question=q)
    return render(request, "qa/base_question.html", { "question": q, "answers": answers })
