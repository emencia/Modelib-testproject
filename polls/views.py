from django.views.generic import TemplateView

# Create your views here.
from .models import Question


class IndexView(TemplateView):
    template_name = 'polls/index.html'

    def questions(self):
        return Question.objects.all()
