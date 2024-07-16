from django.contrib import admin
from . import models

# Register and configure the Category model in the admin site.
@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    """
    Admin configuration class for the Category model.
    """
    list_display = [
        'name',
    ]

# Register and configure the Quiz model in the admin site.
@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    """
    Admin configuration class for the Quiz model.
    """
    list_display = [
        'id', 
        'title',
    ]

# Class that defines an inline for the Answer model, to be used within Question.
class AnswerInlineModel(admin.TabularInline):
    """
    Inline admin configuration for including answers (Answer) in the Question model view.
    """
    model = models.Answer
    fields = [
        'answer_text', 
        'is_right'
    ]

# Register and configure the Question model in the admin site.
@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Admin configuration class for the Question model.
    """
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title', 
        'quiz',
        'date_updated'
    ]
    inlines = [
        AnswerInlineModel, 
    ]

# Register and configure the Answer model in the admin site.
@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    """
    Admin configuration class for the Answer model.
    """
    list_display = [
        'answer_text', 
        'is_right', 
        'question'
    ]
