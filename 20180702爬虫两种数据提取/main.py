# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:14:02 2018

@author: zdc
"""
import os
import pandas as pd
import numpy as np

abs_dir = r'C:\Program Files (x86)\Microsoft Visual Studio\Shared\Anaconda3_64'

def read_txt(file_abs_dir:str)  -> list:
    ''' 
    读取文件所有行，返回list
    '''
    if os.path.isfile(file_abs_dir):
        with open(file_abs_dir,encoding='utf-8') as f:
            res = f.readlines()
    return res

def judge_pure_english(eng_str):
    """
    判断是否英文
    177为±，此处只能看报错然后加上
    """
    return all(ord(c) < 128 or ord(c) == 177 for c in eng_str)

def is_input1(input1):
    pass
    
    
def deal_with_input1(input1:str) -> pd.DataFrame:
    '''
    以<span#lblresult > table开头的
    '''
    #input1 = ipt[11][span:]
    #转化为list
    ipt1_list = input1.split('<n>')
    
    #返回结果
    temp = ""
    res_English = []
    res_Chinese = []
    
    #循环list中所有的元素
    for i in range(0,len(ipt1_list)):
        if i != 0:
            #print(i,temp)
            #两行不同并且第i行长度应该大于3
            if judge_pure_english(ipt1_list[i]) ^ judge_pure_english(ipt1_list[i-1]) and len(ipt1_list[i])>3:
                if judge_pure_english(ipt1_list[i]):
                    temp = temp.replace(" ","")
                    res_Chinese.append(temp)
                else:
                    res_English.append(temp)
                temp = ''
        temp = temp + ipt1_list[i]
    
    #处理最后一行汉字
    if temp:
        res_Chinese.append(temp)
        temp = ""
    
    if res_Chinese and res_English:
        #删除开头的Chinese空行：
        if len(res_Chinese[0]) <= 3:
            res_Chinese.pop(0)

        #删除过短的结尾行
        if len(res_Chinese) == len(res_English) + 1:
            res_Chinese.pop(-1)
        
        if len(res_Chinese) == len(res_English) - 1:
            res_English.pop(-1)
        
        if not temp and len(res_Chinese) == len(res_English):
            return pd.DataFrame(columns=["English","Chinese"],
                                data=np.transpose([res_English,res_Chinese]))
    
    
if __name__ == '__main__':
    #读取
    output_path = r"D:\ljqProject\20180702爬虫两种数据提取"
    ipt = read_txt(r"D:\ljqProject\20180702爬虫两种数据提取\uniq_net_cnki_dict_E053.txt")
    res = pd.DataFrame(columns=["English","Chinese"])
    i = 1
    table = len("<table[id^=showjd_] >")
    span = len("<span#lblresult > table >监督<n> ")
    for line in ipt:
        print(i)
        i = i + 1
        if line.startswith("<span"):
            res = res.append(deal_with_input1(line[span:]),ignore_index=True)
        elif line.startswith("<table"):
            line_list = line.split("短句来源")[:-1]
            for line in line_list:
                res = res.append(deal_with_input1(line[table:]),ignore_index=True)
        if len(res.index) > 25000:
            res.to_csv(os.path.join(output_path,str(i)+".csv"),
                       encoding = "UTF8",
                       index = False,
                       sep = "^")
            res = pd.DataFrame(columns=["English","Chinese"])

