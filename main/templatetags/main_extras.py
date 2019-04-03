from django import template
from django.forms import CheckboxInput, CheckboxSelectMultiple
from django.urls import reverse_lazy


register = template.Library()


@register.filter(name='leader')
def get_leader(value, value2):
    if value2 is None:
        if value is None:
            return -1
        else:
            return value
    elif value is None:
        return value2
    else:
        if value >= value2:
            return value
        else:
            return value2


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return isinstance(field.field.widget, CheckboxInput)


@register.filter(name='is_mult_choice')
def is_multiple_choice(field):
    return isinstance(field.field.widget, CheckboxSelectMultiple)


@register.filter(name='url')
def make_ref(value):
    name = value.__class__.__name__.lower()
    return reverse_lazy(
        f'{name}',
        kwargs={'pk': value.id}
    )
