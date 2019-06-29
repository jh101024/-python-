#encoding:utf-8
def insert_sort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        #while j>=0 and list[j]>key:##正确的插入排序
        while j > 0 and list[j] > key:##错误的插入排序（举例）
            list[j+1]=list[j]
            j=j-1
        list[j+1]=key
    return list

def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1,i,-1):
            if list[j]<list[j-1]:
                list[j-1],list[j]=list[j],list[j-1]
    return list


if __name__ == '__main__':
    ##错误结果：
    A=[3,1]
    a = insert_sort(A)
    b = bubble_sort(A)
    print("插入排序的结果为：", a)
    print("冒泡排序的结果为：", b)

    #正确结果：
    A=[3,1]
    a=insert_sort(A)
    print("插入排序的结果为：",a)
    B=[3,1]
    b=bubble_sort(B)
    print("冒泡排序的结果为：",b)
