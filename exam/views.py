from django.views import generic
from .models import Exam


class ExamsListView(generic.ListView):
    model = Exam
    context_object_name = 'exams'
    template_name = 'exam/exam-list.html'


class ExamsDetailView(generic.DetailView):
    model = Exam
    context_object_name = 'exam-detail'
    template_name = 'exam/exam-list.html'
