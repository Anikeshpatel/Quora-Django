from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect('/auth')
    return render(request,'feed.html', {
        'title': 'Who wrote the google search algorithm?',
        'desc': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Possimus quis hic expedita voluptate earumodit voluptas\n' +
        '    eveniet in est aperiam, natus architecto illo ad vitae, aliquam nostrum? Minima,eius quae. Lorem ipsum, dolor sit\n' +
        '    amet consectetur adipisicing elit. Possimus quis hic expedita voluptate earum odit voluptas eveniet in est aperiam,\n' +
        '    natus architecto illo ad vitae, aliquamnostrum? Minima, eius quae.',
        'likes': 100,
        'time': 'Asked 1 hr ago',
        'usrName': 'UserName',
        'listData': [0,2,4,5,6,7,65,4,4,3,3,4,5,6,7,8,8]
    })

def question(request):
    if not request.user.is_authenticated:
        return redirect('/auth')
    return render(request, 'question.html', {})

def answer(request):
    if not request.user.is_authenticated:
        return redirect('/auth')
    return render(request, 'answer.html', {})
