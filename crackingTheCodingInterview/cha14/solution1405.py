"""
Explain what object reflection is in Java and why it is useful.

analyze:
in python
>>> [x for x in dir(1) if callable(getattr(1, x))]
1 is an instance of built-in type int, dir() will get instance's all
attrs, filter by callable will get all method of int instance.

this is useful when you need to know if an instance has some method,
or it can be used when debug
"""
