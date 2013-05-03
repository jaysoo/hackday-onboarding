import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'waveonboarder.settings'

project = 'server/'
workspace = os.path.dirname(project)
sys.path.append(workspace)

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
