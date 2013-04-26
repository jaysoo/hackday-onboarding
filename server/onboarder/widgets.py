from django.forms import Select, TextInput
from django.utils.safestring import mark_safe


class CombinedButtonInput(TextInput):
    def __init__(self, prepend=None, append=None, attrs=None):
        super(CombinedButtonInput, self).__init__(attrs)
        self.prepend, self.append = prepend, append

    def render(self, name, value, attrs=None):
        elements = {
            'prepend': '',
            'append': ''
        }
        classes = []

        if self.prepend:
            classes.append(u'input-prepend')
            elements['prepend'] = self.prepend

        if self.append:
            classes.append(u'input-append')
            elements['append'] = self.append

        elements['input'] = super(CombinedButtonInput, self).render(name, value, attrs)
        elements['classes'] = ' '.join(classes)
        
        return mark_safe(u'<div class="{classes}">{prepend}{input}{append}</div>' \
            .format(**elements))