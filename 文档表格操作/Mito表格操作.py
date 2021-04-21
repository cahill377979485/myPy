#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2021/4/21 10:06
# @File : Mito表格操作.py
# @Author:
# import Python packages
import mitosheet
import pandas as pd

# Create a simple dataframe to display
car_data = pd.DataFrame({'car': ['Toyota', 'Nissan', 'Honda', 'Mini Cooper', 'Saturn'], 'mph': [60, 50, 60, 75, 90], 'length': [10, 12, 13, 8, 9]})

# render the Mitosheet with car_data
mitosheet.sheet(car_data)