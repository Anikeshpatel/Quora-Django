from django.urls import path
from .views import home, question, answer

urlpatterns = [
    path('', home, name='home'),
    path('question', question, name='question'),
    path('answer', answer, name='answer')
]
