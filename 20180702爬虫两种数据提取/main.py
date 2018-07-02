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

def is_contain_Chinese(uchar:str) -> bool:

    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False
    
def deal_with_input1(input1:str) -> pd.DataFrame:
    '''
    以<span#lblresult > table开头的
    '''
    #转化为list
    ipt1_list = input1.split('<n>')
    
    #返回结果
    temp = ""
    res_English = []
    res_Chinese = []
    
    for i in range(1,len(ipt1_list)):
        print(i,temp)
        if judge_pure_english(ipt1_list[i]) ^ judge_pure_english(ipt1_list[i-1]):
            if judge_pure_english(ipt1_list[i]):                
                res_Chinese.append(temp)
            else:
                res_English.append(temp)
            temp = ''
        temp = temp + ipt1_list[i]
    
    #处理最后一行汉字
    if temp:
        res_Chinese.append(temp)
        temp = ""
        
    if not temp:
        return pd.DataFrame(data=np.transpose([res_English,res_Chinese[1:]]))
    
    
if __name__ == '__main__':
    #读取
    input1 = read_txt(r"D:\ljqProject\20180702爬虫两种数据提取\input1.txt")[0]
    input2 = read_txt(r"D:\ljqProject\20180702爬虫两种数据提取\input2.txt")[0]
    
    input1_res = deal_with_input1(input1)
            