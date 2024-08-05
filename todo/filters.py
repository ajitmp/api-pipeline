#todo/filters.py
import django_filters
from .models import ToDo
                            
class ToDoFilter(django_filters.FilterSet):
    class Meta:
        model = ToDo
        fields = ['task','completed']