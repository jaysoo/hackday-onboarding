from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

import onboarder.views as views
from api.views import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/tasks/(?:(?P<instance_id>\d+)/)?$', TaskResourceView.as_view(), name='api-task-resource'),
    url(r'^api/badges/(?:(?P<instance_id>\d+)/)?$', BadgeResourceView.as_view(), name='api-badge-resource'),
    url(r'^api/login/?$', LoginResourceView.as_view(), name='api-login-resource'),
    url(r'^api/logout/?$', LogoutResourceView.as_view(), name='api-logout-resource'),

    url(r'^auth/', include('auth.urls', namespace='auth')),

    url(r'^tasks/add/$', login_required(views.AddTaskView.as_view()), name='add_task'),
    url(r'^tasks/(?P<pk>\d+)/edit/$', login_required(views.EditTaskView.as_view()), name='edit_task'),
    url(r'^tasks/(?P<pk>\d+)/delete/$', login_required(views.DeleteTaskView.as_view()), name='delete_task'),
    url(r'^tasks/(?P<pk>\d+)/move-up/$', login_required(views.MoveUpView.as_view()), name='move_up'),
    url(r'^tasks/(?P<pk>\d+)/move-down/$', login_required(views.MoveDownView.as_view()), name='move_down'),
    url(r'^tasks/$', login_required(views.TasksView.as_view()), name='tasks'),

    url(r'^profiles/add/$', login_required(views.AddProfileView.as_view()), name='add_profile'),
    url(r'^profiles/(?P<pk>\d+)/edit/$', login_required(views.EditProfileView.as_view()), name='edit_profile'),
    url(r'^profiles/(?P<profile_id>\d+)/delete/$', login_required(views.EditProfileView.as_view()), name='delete_profile'),
    url(r'^profiles/$', login_required(views.ProfilesView.as_view()), name='profiles'),

    url(r'^recruits/add/$', login_required(views.AddRecruitView.as_view()), name='add_recruit'),
    url(r'^recruits/(?P<pk>\d+)/edit/$', login_required(views.EditRecruitView.as_view()), name='edit_recruit'),

    url(r'^random-facts/$', login_required(views.FactsView.as_view()), name='facts'),
    url(r'^random-facts/add/$', login_required(views.AddFactView.as_view()), name='add_fact'),
    url(r'^random-facts/(?P<pk>\d+)/edit/$', login_required(views.EditFactView.as_view()), name='edit_fact'),
)
