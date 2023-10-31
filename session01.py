import numpy as np
import math
import matplotlib.pyplot as plt
def sort(arg):
    length=len(arg)
    for i in range(0,length-1):
        for j in range(i+1,length):
            if(arg[i]>arg[j]):
                tmp=arg[i]
                arg[i]=arg[j]
                arg[j]=tmp
    return arg
def tbc(lists):
   total = sum(lists)
   length = len(lists)
   result = total/length
   return result
n = int(input('Nhập số tự nhiên n: '))
list=[]
for i in range(0,n):
    temp=int(input())
    list.append(temp)
print("mảng sắp xếp tăng dần",sort(list))
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]
response=tbc(list)
print("giá trị trung bình",response)
print("số gần nhất với giá tri trung bình",find_nearest(list,response))

