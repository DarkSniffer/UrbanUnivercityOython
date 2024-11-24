import inspect
import types
from pprint import pprint


def introspection_info(obj):
    info = {}

    # Тип объекта
    info['type'] = type(obj).__name__

    # Атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

    # Методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    # Модуль, к которому принадлежит объект
    info['module'] = getattr(obj, '__module__', None)

    # Дополнительные свойства
    if isinstance(obj, types.FunctionType):
        info['signature'] = inspect.signature(obj)
        info['source_code'] = inspect.getsource(obj)
    elif isinstance(obj, (list, tuple, set, frozenset)):
        info['length'] = len(obj)
    elif isinstance(obj, dict):
        info['keys'] = list(obj.keys())

    return info


# Пример использования
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value * 2


my_obj = MyClass(10)
obj_info = introspection_info(my_obj)
pprint(obj_info)

number_info = introspection_info(42)
pprint(number_info)
