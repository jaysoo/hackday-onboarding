import sys

from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist

from forms import TaskForm, ProfileForm, RecruitForm, FactForm
from models import Task, Profile, NewRecruit, RandomFact, Choice


class TasksView(ListView):
    template_name = 'onboarder/tasks.html'
    model = Task
    context_object_name = 'tasks'



class AddTaskView(FormView):
    template_name = 'onboarder/add_task.html'
    form_class = TaskForm

    def form_valid(self, form):
        task = form.instance
        try:
            last_task = Task.objects.order_by('-number')[0]
            task.number = last_task.number + 1
        except IndexError:
            task.number = 0

        task.save()

        task.profiles.add(*form.cleaned_data['profiles'])
        
        for choice in ['choice1', 'choice2', 'choice3', 'choice4']:
            if form.cleaned_data[choice]:
                Choice.objects.create(text=form.cleaned_data[choice],
                    correct=form.cleaned_data['correct_choice'] == choice[-1],
                    task=task)

        return redirect(reverse('tasks'))


class EditTaskView(UpdateView):
    template_name = 'onboarder/edit_task.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'task'

    def get_initial(self):
        initial = super(EditTaskView, self).get_initial()
        task = self.get_object()
        initial['profiles'] = task.profiles.all()
        for c, i in zip(task.choices.all(), xrange(1, sys.maxint)):
            initial['choice' + str(i)] = c.text
            if c.correct:
                initial['correct_choice'] = str(i)
        return initial

    def get_context_data(self, **kwargs):
        context = super(EditTaskView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        task = form.instance
        task.save()

        # this is ghetto, I know
        task.profiles.clear()
        task.profiles.add(*form.cleaned_data['profiles'])
        task.choices.clear()

        for choice in ['choice1', 'choice2', 'choice3', 'choice4']:
            if form.cleaned_data[choice]:
                Choice.objects.create(text=form.cleaned_data[choice],
                    correct=form.cleaned_data['correct_choice'] == choice[-1],
                    task=task)

        return redirect(reverse('tasks'))


class DeleteTaskView(View):
    def get(self, request, pk):
        Task(pk=pk).delete()
        return redirect(reverse('tasks'))


class MoveUpView(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        if task.number:
            task_above = Task.objects.get(number=task.number-1)
            task_above.number, task.number = task.number, task_above.number
            task_above.save()
            task.save()
        return redirect(reverse('tasks'))

class MoveDownView(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        try:
            task_below = Task.objects.get(number=task.number+1)
            task_below.number, task.number = task.number, task_below.number
            task_below.save()
            task.save()
        except ObjectDoesNotExist:
            pass
        
        return redirect(reverse('tasks'))

class ProfilesView(ListView):
    template_name = 'onboarder/profiles.html'
    model = Profile
    context_object_name = 'profiles'


class AddProfileView(CreateView):
    template_name = 'onboarder/add_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profiles')


class EditProfileView(UpdateView):
    template_name = 'onboarder/edit_profile.html'
    form_class = ProfileForm
    model = Profile
    context_object_name = 'profile'
    success_url = reverse_lazy('profiles')


class AddRecruitView(CreateView):
    template_name = 'onboarder/add_recruit.html'
    form_class = RecruitForm
    success_url = reverse_lazy('profiles')
    

class EditRecruitView(UpdateView):
    template_name = 'onboarder/edit_recruit.html'
    form_class = RecruitForm
    model = NewRecruit
    context_object_name = 'recruit'
    success_url = reverse_lazy('profiles')


class FactsView(ListView):
    template_name = 'onboarder/facts.html'
    model = RandomFact
    context_object_name = 'facts'


class AddFactView(CreateView):
    template_name = 'onboarder/add_fact.html'
    form_class = FactForm
    success_url = reverse_lazy('facts')


class EditFactView(UpdateView):
    template_name = 'onboarder/edit_fact.html'
    form_class = FactForm
    model = RandomFact
    context_object_name = 'fact'
    success_url = reverse_lazy('facts')
