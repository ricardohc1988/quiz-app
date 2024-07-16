from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Quiz, Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer

class Quiz(generics.ListAPIView):
    """
    API view that returns a list of all quizzes.

    Attributes:
        queryset (QuerySet): The queryset containing all Quiz objects.
        serializer_class (Serializer): The serializer class used to serialize Quiz objects.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
class RandomQuestion(APIView):
    """
    API view that returns a random question for a given quiz topic.

    Methods:
        get(request, **kwargs):
            Retrieves a random question for the specified quiz topic and returns it serialized.
        
    Args:
        request (HttpRequest): The request object.
        **kwargs (dict): Additional keyword arguments, expects 'topic' to be provided.
    
    Returns:
        Response: Serialized data of the random question.
    """
    def get(self, request, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)
    
class QuizQuestion(APIView):
    """
    API view that returns all questions for a given quiz topic.

    Methods:
        get(request, **kwargs):
            Retrieves all questions for the specified quiz topic and returns them serialized.
        
    Args:
        request (HttpRequest): The request object.
        **kwargs (dict): Additional keyword arguments, expects 'topic' to be provided.
    
    Returns:
        Response: Serialized data of all questions for the quiz topic.
    """
    def get(self, request, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)