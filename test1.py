#!/usr/bin/env python
# _*_ coding: utf-8 _*_
_metaclass_ = type
class Person:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        return  "Hello world! I'm %s." % self.name

foo = Person()
bar = Person()
foo.setName('rongkeke')
bar.setName('zhangtingting')

print '======='
print bar.greet()
print foo.greet()


 