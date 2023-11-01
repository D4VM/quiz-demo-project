from django.urls import path
from django.urls import include, re_path
from . import views

urlpatterns = [
    # path('exam-list', view=exam_list, name='exam_list'),
    re_path(r'^exam-list/$', views.ExamsListView.as_view(), name='exams'),
    re_path(r'^exam-list/(?P<pk>\d+)$', views.ExamsDetailView.as_view(), name='exam-detail'),


]
