import inspect
import sys

def introspection_info(obj):
    ars = obj
    info = {}


    info['type'] = type(ars)
    info['attributes'] = ars
    info['methods'] = dir(ars)
    info['module'] = inspect.getmodule(introspection_info)
    return info


number_info = introspection_info(42)
print(number_info)
