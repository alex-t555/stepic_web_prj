"""
    qa/views.py
"""
from django import http
from django import shortcuts
# from django import views
from django.views.decorators.http import require_GET
from django import core
from django import db
from django import contrib

from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
# from qa.forms import SignupForm
from qa.forms import UserRegistrationForm


def paginate(request: http.HttpRequest, qs: db.models.QuerySet) -> core.paginator.Page:
    """
    pagination method
    """
    try:
        limit = int(request.GET.get('limit', 10))
        page = int(request.GET.get('page', 1))
    except ValueError as e:
        raise http.Http404 from e
    limit = min(limit, 100)
    paginator = core.paginator.Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except core.paginator.EmptyPage:
        page = paginator.page(paginator.num_pages())
    return page


def test(_: http.HttpRequest) -> http.HttpResponse:
    """ test method """
    return http.HttpResponse('200 OK')


@require_GET
def home(request: http.HttpRequest) -> http.HttpResponse:
    """
    URL = /?page=2
    """
    qs = Question.objects.new()
    page = paginate(request, qs)
    return shortcuts.render(request, "qa/home.html", { "page": page })


@require_GET
def popular(request: http.HttpRequest) -> http.HttpResponse:
    """
    URL = /popular/?page=3
    """
    qs = Question.objects.popular()
    page = paginate(request, qs)
    return shortcuts.render(request, "qa/popular.html", { "page": page })


def question(request: http.HttpRequest, id_question: str) -> http.HttpResponse:
    """
    URL = /question/5/
    """
    q = shortcuts.get_object_or_404(Question, id=id_question)
    answers = Answer.objects.filter(question=q)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.question = q
            a.author = request.user
            a.save()
            return http.HttpResponseRedirect(request.get_raw_uri())
    else:
        form = AnswerForm()
    return shortcuts.render(request, "qa/question.html",
                            { "question": q, "answers": answers, "form": form })


def ask(request: http.HttpRequest) -> http.HttpResponse:
    """
    URL = /ask/
    """
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.author = request.user
            q.save()
            url = q.get_absolute_url()
            return http.HttpResponseRedirect(url)
    else:
        form = AskForm(initial={"author": request.user})
    return shortcuts.render(request, "qa/ask.html", { "form": form })


def signup(request: http.HttpRequest) -> http.HttpResponse:
    """
    URL = /signup/
    """
    # if request.method == "POST":
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         contrib.auth.login(request, user)
    #         # return http.HttpResponseRedirect("/")
    #         return shortcuts.redirect("home")
    # else:
    #     form = SignupForm()
    # return shortcuts.render(request, "qa/base_form.html", { "form": form })

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data.get('password')
            user.save()
            contrib.auth.login(request, user)
            return shortcuts.redirect("home")
    else:
        form = UserRegistrationForm()
    return shortcuts.render(request, "qa/base_form.html", { "form": form })


def login(request: http.HttpRequest) -> http.HttpResponse:
    """
    URL = /login/
    """
    if request.method == "POST":
        form = contrib.auth.forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                contrib.auth.login(request, user)
                # return http.HttpResponseRedirect("/")
                return shortcuts.redirect("home")
    else:
        form = contrib.auth.forms.AuthenticationForm()
    return shortcuts.render(request, "qa/base_form.html", { "form": form })


def logout(request: http.HttpRequest) -> http.HttpResponse:
    contrib.auth.logout(request)
    # return http.HttpResponseRedirect("/")
    return shortcuts.redirect("home")
