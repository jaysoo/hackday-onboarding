import django.forms as forms
from django.forms.models import ModelMultipleChoiceField

from models import Task, Profile, NewRecruit, RandomFact
from widgets import CombinedButtonInput

INACTIVE_QUESTION = '<a href="#" class="btn btn-danger" data-toggle="{}" tabindex="-1"><i class="icon-remove"></i></a>'

class TaskForm(forms.ModelForm):
    choice1 = forms.CharField(max_length=250, label='', required=False,
        widget=CombinedButtonInput(prepend=INACTIVE_QUESTION.format(1)))
    choice2 = forms.CharField(max_length=250, label='', required=False,
        widget=CombinedButtonInput(prepend=INACTIVE_QUESTION.format(2)))
    choice3 = forms.CharField(max_length=250, label='', required=False,
        widget=CombinedButtonInput(prepend=INACTIVE_QUESTION.format(3)))
    choice4 = forms.CharField(max_length=250, label='', required=False,
        widget=CombinedButtonInput(prepend=INACTIVE_QUESTION.format(4)))
    
    correct_choice = forms.CharField(max_length=1, widget=forms.HiddenInput(),
        initial=1)
    profiles = forms.ModelMultipleChoiceField(queryset=Profile.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'unstyled'}))

    class Meta:
        model = Task
        widgets = {
            'description': forms.widgets.Textarea()
        }
        exclude = ('number')

    def clean_correct_choice(self):
        choice = self.cleaned_data['correct_choice']
        choices = [ self.cleaned_data['choice1'], self.cleaned_data['choice2'],
                self.cleaned_data['choice3'], self.cleaned_data['choice4']]
        c_int = int(choice) - 1

        if c_int < 0 or c_int > 3:
            self._errors['correct_choice'] = "Invalid choice"

        if [ c for c in choices if c ] and not choices[c_int]:
            self._errors['correct_choice'] = "Correct choice is blank"

        return choice


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile


class RecruitForm(forms.ModelForm):
    class Meta:
        model = NewRecruit


class FactForm(forms.ModelForm):
    class Meta:
        model = RandomFact