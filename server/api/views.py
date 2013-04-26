from django.utils import simplejson as json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import View
from django.core.serializers.python import Serializer as PythonSerializer
from django.http import HttpResponse, Http404

from onboarder.models import Task, NewRecruit


class Resource(object):
  def authenticate(self, request):
    if 'user' in request.session:
      return
    raise Http404

  def to_json(self, obj_list):
    """
    Takes a output from django.core.serializers.python.Serializer
    and converts to the expected flat object format.
    """
    r_list = []

    for obj in obj_list:
      r_obj = {'id': obj['pk']}
      r_obj = dict(r_obj.items() + obj['fields'].items())
      r_list.append(r_obj)

    return json.dumps(r_list, cls=DjangoJSONEncoder)


class LoginResourceView(View, Resource):
    serializer = PythonSerializer()

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(LoginResourceView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
      data = json.loads(request.body)
      email = data['email']
      qset = NewRecruit.objects.filter(email=email)

      if qset.exists():
        user = qset[0]
        request.session['user'] = user
        rval = {
          "success": True,
          "user": {
            "email": user.email,
            "name": user.name,
          },
        }
          
        return HttpResponse(json.dumps(rval), mimetype='application/json', status=200)

      rval = {
        "success": False,
      }
        
      return HttpResponse(json.dumps(rval), mimetype='application/json', status=401)

class LogoutResourceView(View, Resource):
    serializer = PythonSerializer()

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(LogoutResourceView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
      del request.session['user']
      return HttpResponse('', mimetype='application/json', status=204)

class TaskResourceView(View, Resource):
    serializer = PythonSerializer()

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(TaskResourceView, self).dispatch(*args, **kwargs)

    def get(self, request, instance_id, *args, **kwargs):
      self.authenticate(request)

      tasks = Task.objects.all()
      tasks_list = self.serializer.serialize(tasks)
      return HttpResponse(self.to_json(tasks_list), mimetype='application/json', status=200)
