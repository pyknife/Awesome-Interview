# -*- coding: cp936 -*-  

import weakref,sys

class TestObj:
    pass


def test_func(reference):
    print 'Hello from Callback function!'

    print reference, 'This weak reference is no longer valid'


a = TestObj()

# ����һ��a��������

x = weakref.ref(a, test_func)

del a  