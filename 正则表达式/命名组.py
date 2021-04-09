#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Python 2.7的手册中的解释：

(?P<name>...)
Similar to regular parentheses, but the substring matched by the group is accessible within the rest of the regular
expression via the symbolic group name name. Group names must be valid Python identifiers, and each group name must be
defined only once within a regular expression. A symbolic group is also a numbered group, just as if the group were not
named. So the group named id in the example below can also be referenced as the numbered group 1.

For example, if the pattern is (?P<id>[a-zA-Z_]\w*),
the group can be referenced by its name in arguments to methods of match objects, such as m.group('id') or m.end('id'),
and also by name in the regular expression itself (using (?P=id))
and replacement text given to .sub() (using \g<id>).

"""
import re


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


def double2(matched):
    value = int(matched.group(1))
    return str(value * 2)


s = 'A23G4HFD567'
# 用命名group的方式
print(re.sub('(?P<value>\\d+)', double, s))  # ?P<value>的意思就是命名一个名字为value的group，匹配规则符合后面的/d+，具体文档看上面的注释
# 用默认的group带数字的方式
print(re.sub('(\\d+)', double2, s))
