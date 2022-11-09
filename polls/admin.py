from django.contrib import admin

# Register your models here.
from . import models


class ChoiceInline(admin.TabularInline):
    model = models.Choice

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]
