from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def cut_url_tag(value: str, arg):
    '''
    Remove url tag vith value from url string
    '''
    start = value.find('&'+str(arg))
    if start == -1:
        start = value.find('?'+str(arg))
        if start == -1:
            return value
    end = value.find('&', start+1)
    if end == -1:
        return value.replace(value[start:], '')
    else:
        return cut_url_tag(value.replace(value[start:end], ''), arg)


@register.filter
@stringfilter
def add_page_tag(value: str, arg):
    '''
    Add page tag vith value in url string
    '''
    value = cut_url_tag(value, 'page')
    if value.find('?') == -1:
        return value+'?page='+str(arg)
    else:
        return value+'&page='+str(arg)
