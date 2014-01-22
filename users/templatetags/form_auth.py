from django import template
from users.forms import CreateUserForm

register = template.Library()

@register.inclusion_tag('users/auth_form.html')
def show_forms():
    return {
        'form'  : CreateUserForm
    }