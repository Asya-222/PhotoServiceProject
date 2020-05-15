from django import template
import json
from ..models import Image
register = template.Library()


@register.filter(name='split')
def split(value, arg):
    ids = value.split(arg)
    resultPath = []
    for target_list in ids:
        try:
            resultPath.append(Image.objects.get(pk=target_list).get_path())
        except:
            pass
    
    return resultPath

@register.filter(name='debug')
def debug(text):
  print(json.dumps(text))
  return ''