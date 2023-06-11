from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})


@register.filter
def divide(value, arg):
    try:
        return int(value) // int(arg)
    except (ValueError, ZeroDivisionError):
        return None

@register.filter
def mod(value, arg):
    try:
        return int(value) % int(arg)
    except (ValueError, ZeroDivisionError):
        return None


