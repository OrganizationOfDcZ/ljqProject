#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 00:39:24 2018

@author: hnjyzdc
"""

import pandas as pd

excel = pd.read_excel('/Users/hnjyzdc/Documents/数据合并.xlsx',header = None)
fl = open('/Users/hnjyzdc/Documents/数据合并.txt', 'w')
for index in excel.index:
    row = excel.iloc[index]
    res = []
    for ele in row.values:
        #这一行代码特别坑，应为单元格内有换行符
        res.append(str(ele).replace("\n",""))
    fl.write('####'.join(res)+'\n')
fl.close()
