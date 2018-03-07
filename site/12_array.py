# -*- coding: UTF-8 -*-

#找出数组中差值为K的数共有几对
def array_diff(arr,d):
    newlst = [i + d for i in arr]
    print(newlst,set(arr)& set(newlst))
    return len(set(arr) & set(newlst))

#找出数组中差值为K的数共有几对

def array_sum(arr,d):
    arr = sorted(arr)
    i = 0
    j = len(arr)-1
    count =0
    print arr,arr[1]
    while(i < j):
        if((arr[i] + arr[j]) < d):
            i+=1
        elif(arr[i] + arr[j] > d):
            j-=1
        else:
            count+=1
            j-=1
    return count

def array_check(arr,d):
    count = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if (arr[j] + arr[i])== d:
                count +=1
    return count

if __name__=='__main__':
    arr = [3,5,8,7,8,10]#7-8 与8-7 数组位置不同 得到的结果不同
    # arr = [7, 6, 23,19,10,11, 9, 3, 15]
    d = 15
    print(array_diff(arr,d))

    k = 15
    print array_sum(arr,k)
    # print array_sum_1(arr,k)
    #
    print array_check(arr, k)
