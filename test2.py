#!/usr/bin/env python
# _*_ coding: utf-8 _*_
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print 'hi,my value is', self.value
class TalkingCalculator(Calculator,Talker):
    pass
tc = TalkingCalculator()
tc.calculate('1+2+3')
tc.talk()
print hasattr(tc, 'talk')