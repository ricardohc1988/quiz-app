from django.urls import path, include
from rest_framework import routers
from .views import Quiz, RandomQuestion, QuizQuestion


urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>', QuizQuestion.as_view(), name='questions'),
]