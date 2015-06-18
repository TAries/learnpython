'''
查找一个序列的平衡点，平衡点前面的和等于后面的和
'''
numbers=[1,5,5,7,1,5,6,2,7,1,4,8,10]
sum=0
balance=0
for i in range(0,len(numbers)):
    #序列求和
    sum=sum+numbers[i]

#用index遍历序列
for index in range(len(numbers)):
    before=0
    after=0
    #分别计算index位置前面和后面数字的和
    for i in range(index):
        before+=numbers[i]
    after=sum-before-numbers[index]

#判断有无找到平衡点
    if before==after:
        balance=1
        break
    else:pass
if balance==1:
    print('the balance is {0} and index is {1}'.format(numbers[index],index+1))
else:print('not found a balance!!!')
