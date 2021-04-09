#!/usr/bin/env python3
# -*- coding:utf-8 -*-




import re

str = "China is a great country"
x = re.search("\s", str)
print(x)
print(x.start())
print(x.end())