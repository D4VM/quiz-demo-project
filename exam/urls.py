from django.urls import path
from django.urls import include, re_path
from . import views

urlpatterns = [
    # path('exam-list', view=exam_list, name='exam_list'),
    # re_path(r'^exam-list/$', views.ExamsListView.as_view()),
    # re_path(r'^exam-list/(?P<pk>\d+)$', views.QuestionListView.as_view()),
    path('exam-list/', views.ExamsListView.as_view()),
    path('exam-list/<int:id>/', views.QuestionListView.as_view()),
    path('exam-list/<int:id>/<int:pk>/', views.AnswerListView.as_view()),

]
