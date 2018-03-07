# -*- coding: UTF-8 -*-

#找出数组中差值为K的数共有几对
def arry(arr,d):
    newlst = [i + d for i in arr]
    print(newlst,set(arr)& set(newlst))
    return len(set(arr) & set(newlst))

if __name__=='__main__':
    arr = [3,5,8,7,8,10]
    d = 2
    print(arry(arr,d))