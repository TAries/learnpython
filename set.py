# coding:utf-8
'''
删除序列中重复的值，类似于set
'''

#源序列
a=[1,5,1,2,7,2,3,3,4,4,5,6,]
#目标序列
b=[]

flag=[]

#生成一个全是0的序列，长度的a相同
for i in range(len(a)):
    flag.append(0)
#遍历序列a，找到重复的值，把flag相应位置的值设成1
for index in range(len(a)):
    for next in a[index+1:]:
        if a[index]==next:
            flag[index]=1

#遍历序列flag，找到值为0的位置，把a相应位置的值append到b中
for index in range(len(flag)):
    if flag[index]==0:
        b.append(a[index])

print(a)
print(flag)
#b.sort()
print(b)
print(set(a))

