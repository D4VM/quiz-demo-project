from django.db import models
from django.urls import reverse


class Exam(models.Model):
    # NOTE: primary_key / pk = id
    title = models.CharField(
        max_length=256,
        verbose_name='name the exam'
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizes'

    # working
    # def get_absolute_url(self):
    #     return "%i/" % self.id

    def get_absolute_url(self):
        return reverse("exam-detail", kwargs={"pk": self.pk})


class Question(models.Model):
    title = models.CharField(max_length=256)
    exam = models.ForeignKey(
        to=Exam,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.title


class Answer(models.Model):
    text = models.CharField(max_length=256)
    is_correct = models.BooleanField()
    question = models.ForeignKey(
        to='Question',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.question.title} / {self.text}'
