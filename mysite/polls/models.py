from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name="date published")

    def _str_(self):
        return f"{self.id}|{self.question_text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def _str_(self):
        return f"{self.id}|{self.question.question_text} | {self.choice_text}"