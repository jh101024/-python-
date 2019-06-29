##该代码实现归并排序
#encoding:utf-8
from math import ceil
def merge(left,right):
    merge_arrays=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merge_arrays.append(left[i])
            i=i+1
        else:
            merge_arrays.append(right[j])
            j=j+1
    if i==len(left):
        merge_arrays.extend(right[j:])
    else:
        merge_arrays.extend(left[i:])
    return merge_arrays
def merge_sort(lists):
    if len(lists)<=1:
        return lists
    array_middle=ceil(len(lists)/2)
    left=merge_sort(lists[:array_middle])
    right=merge_sort(lists[array_middle:])
    result=merge(left,right)
    return result
A=[1,5,3,6,2,9,8,3,7,5,0]
result=merge_sort(A)
print("归并排序后的结果为：",result)