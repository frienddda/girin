from django import template
    
register = template.Library()  
    
@register.simple_tag
def my_tag():
    print("temp test")
    return "Hello World from my_tag() test."
