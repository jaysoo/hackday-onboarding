from django.utils.encoding import smart_unicode, is_protected_type
from django.core.serializers import python, json


class PythonSerializer(python.Serializer):
    def handle_field(self, obj, field):
        """
        Most of this code is codied from Django's python serializer.
        It removes '_pk' from fields' keys
        """
        value = field._get_val_from_obj(obj)
        field_name = field.name
        if field_name[-3:] == '_pk':
            field_name = field_name[:-3]
        # Protected types (i.e., primitives like None, numbers, dates,
        # and Decimals) are passed through as is. All other values are
        # converted to string first.
        if is_protected_type(value):
            self._current[field_name] = value
        else:
            self._current[field_name] = field.value_to_string(obj)

    def end_object(self, obj):
        self._current['id'] = smart_unicode(obj._get_pk_val(), strings_only=True)
        self.objects.append(self._current)
        self._current = None

    def handle_fk_field(self, obj, field):
          id = getattr(obj, '%s_id' % field.name)
          self._current['%s_id' % field.name] = smart_unicode(id, strings_only=True)

    def handle_m2m_field(self, obj, field):
          m2m_value = lambda value: smart_unicode(value._get_pk_val(), strings_only=True)
          self._current[field.name] = [m2m_value(related) for related in getattr(obj, field.name).iterator()]


class JSONSerializer(json.Serializer, PythonSerializer):
    pass
