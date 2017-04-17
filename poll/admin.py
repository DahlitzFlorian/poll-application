from django.contrib import admin
from .models import Question, Choice


# class providing choice related to question
# class ChoiceInline(admin.StackedInline) -> stacked form
# the following provides it as table
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# class to customize question model in admin panel
class QuestionAdmin(admin.ModelAdmin):
    # classify the add and change pages into fieldsets
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date information', {'fields' : ['pub_date']})
    ]
    inlines = [ChoiceInline]

    # customizes the shown table on the 'show all'/'changes'-page
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # add list filters at the sidebar
    list_filter = ['pub_date']

    # add search capabilities
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
