#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    checks if object is *only* a subclass
    """
    return(type(obj) != a_class and isinstance(obj, a_class))
