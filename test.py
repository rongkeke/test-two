#!/usr/bin/env python
# _*_ coding: utf-8 _*_
def print_param(*param):
    print param
print_param('Testing')

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
def lookup (data, label, name):
    return data[label].get(name)
# print lookup(storage,'middle','Lie')
def store(data, *full_name):
    for full_name in full_name:
        names = full_name.split()  # full_name = 'Magnus Lie Hetland'
        print 'names =', names  # names = ['Magnus', 'Lie', 'Hetland']
        if len(names) == 2: names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name, in zip(labels, names):  # zip=[('first', 'Magnus'), ('middle', 'Lie'), ('last', 'Hetland')]
            people = lookup(data, label, name)  # 这一步获得了magnus lie hetland
        # print 'people = ', people
            if people:
                people.append(full_name)
            else:
              data[label][name] =[full_name]
              print 'data= ', data
    print "all data = ", data
d = {}
init(d)
store(d, 'Luke Skywalker', 'Anak in Skywalker')
lookup(d, 'last', 'Anak in Skywalker')
print d['last']['Skywalker']
print lookup(d, 'last', 'Skywalker')


"""
Mynames = {}
init(Mynames)
# print lookup(storage,'middle','Lie')
# print 'Mynames= ', Mynames
store(Mynames, 'Magnus Lie Hetland')
print lookup(Mynames, 'middle', 'Lie')
"""
print map(str, range(10))
def func(x):
    return x.isalnum()
seq = ["foo", "x41", "?!", "***"]
print filter(func, seq)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print reduce(lambda x, y: x+y, numbers)
