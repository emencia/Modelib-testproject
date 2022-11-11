from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, TemplateView, View

# Create your views here.
from .models import Question
from .forms import VoteForm


class IndexView(TemplateView):
    template_name = 'polls/index.html'

    def questions(self):
        return Question.objects.all()


class VoteView(FormView, DetailView):
    template_name = 'polls/vote.html'
    model = Question
    form_class = VoteForm
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        self.object = self.get_object()

        # Increment the votes
        pk = form.cleaned_data['choice']
        choice = self.object.choice_set.get(pk=pk)
        choice.votes += 1
        choice.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        self.object = self.get_object()
        return super().form_invalid(form)


class GetDataView(View):

    def get(self, request, pk):
        obj = get_object_or_404(Question, pk=pk)

        choices = []
        for choice in obj.choice_set.all():
            choices.append({
                'choice_text': choice.choice_text,
                'votes': choice.votes,
            })

        return JsonResponse({
            'question_text': obj.question_text,
            'choices': choices,
        })
