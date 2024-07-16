from django.db import models
from django.contrib.auth.models import User 

class Category(models.Model):
    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    class Meta:
        verbose_name = ('Quiz')
        verbose_name_plural = ('Quizzes')
        ordering = ['id']

    title = models.CharField(max_length=250, default='New Quiz', verbose_name='Quiz Title')
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Updated(models.Model):
    date_updated = models.DateTimeField(
        verbose_name=('Last Updated'), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    class Meta:
        verbose_name = ('Question')
        verbose_name_plural = ('Questions')
        ordering = ['id']

    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, verbose_name=('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=('Created At'))
    is_active = models.BooleanField(default=False, verbose_name=('Active Status'))

    def __str__(self):
        return self.title

class Answer(Updated):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=('Answer Text'))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text