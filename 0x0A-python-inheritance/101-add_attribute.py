#!/usr/bin/python3
def add_attribute(class_name, attr_name, inst_name):
    if hasattr(class_name, attr_name):
        raise TypeError("can't add new attribute")
    class_name.attr_name = inst_name
