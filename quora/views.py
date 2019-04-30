from django.shortcuts import render, redirect

from .models import Question, Answer
# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect('/auth')

    if request.POST:
        que = Question()
        que.question = request.POST['question']
        que.author = request.user
        que.save()
        print("Question added to database")

    ctx = {
        "user": request.user,
        "answers": Answer.objects.all()
    }
    for ans in ctx['answers']:
        ans.answer.replace('\n', '<br />')
    return render(request, 'feed.html', ctx)


def question(request):
    if not request.user.is_authenticated:
        return redirect('/auth')

    ctx = {
        'questions': Question.objects.filter(author=request.user)
    }
    return render(request, 'question.html', ctx)


def answer(request):
    if not request.user.is_authenticated:
        return redirect('/auth')
    return render(request, 'answer.html', {})
