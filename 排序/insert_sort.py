##该代码实现插入排序算法
#encoding:utf-8

#升序（从小到大排序）
# a=[5,2,4,6,1,3]
a=[1,3,7,5,4,8,2,0,9,6]
# a=[1,2,3,2,1,5,7,5,8,9,0,2,1]
print("插入排序前（升序）：",a)
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
print("插入排序后（升序）：",a)


#sorted实现
a=[1,2,3,2,1,5,7,5,8,9,0,2,1]
print("sorted排序前（升序）：",a)
print("sorted排序后（升序）：",sorted(a))











