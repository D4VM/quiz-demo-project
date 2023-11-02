from django.views import generic
from .models import Exam, Question, Answer


class ExamsListView(generic.ListView):
    model = Exam
    context_object_name = 'exam_list'
    template_name = 'exam/exam-list.html'


class QuestionListView(generic.ListView):
    model = Question
    context_object_name = 'question_list'
    template_name = 'exam/question-list.html'


class AnswerListView(generic.ListView):
    model = Answer
    context_object_name = 'answer_list'
    template_name = 'exam/answer-list.html'
