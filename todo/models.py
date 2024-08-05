from django.db import models
#python manage.py loaddata todo/fixtures/todo/todo
#https://learndjango.com/tutorials/django-fixtures-dumpdata-loaddata
class ToDo(models.Model):
    task = models.CharField(max_length=2048)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
