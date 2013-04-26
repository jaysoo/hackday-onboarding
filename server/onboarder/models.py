from django.db import models


class Badge(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    
    def __unicode__(self):
        return u'{}'.format(self.name)


class Task(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    pre_step = models.BooleanField(default=False)
    badge = models.ForeignKey(Badge, blank=True, null=True, related_name='tasks')
    image = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['number']

class Profile(models.Model):
    name = models.CharField(max_length=50, verbose_name='Profile name')
    tasks = models.ManyToManyField(Task, related_name='profiles', blank=True)

    def member_list(self):
        return self.members.all()

    def total_tasks(self):
        return self.tasks.count()

    def __unicode__(self):
        return u'{}'.format(self.name)


class NewRecruit(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    start_date = models.DateField()
    job_title = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, related_name='members')

    def tasks_completed(self):
        return self.responses.count()

    def __unicode__(self):
        return u'{}'.format(self.name)


class Choice(models.Model):
    text = models.CharField(max_length=250)
    correct = models.BooleanField(default=False)
    task = models.ForeignKey(Task, related_name='choices', null=True)


class TaskStatus(models.Model):
    task = models.ForeignKey(Task, related_name='tasks', null=True)
    recruit = models.ForeignKey(NewRecruit, related_name='responses')
    complete = models.BooleanField(default=False)
    response = models.CharField(max_length=200, blank=True)


class RandomFact(models.Model):
    person = models.CharField(max_length=50)
    fact = models.CharField(max_length=250)
    picture = models.CharField(max_length=250)

