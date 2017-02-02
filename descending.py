#-*- coding: utf-8 -*-

num = [11, 4, 2, 5, 9, 0, 3, 1]

print("ソート前:{}".format(num))

#Search minimum number
for i in range(len(num)-1):
    min = num[i]
    t = i
    #Compare number
    for j in range((i+1), len(num)):
        if(min < num[j]):
            min = num[j]
            t = j
    #Exchange number
    tmp = num[i]
    num[i] = num[t]
    num[t] = tmp

print("ソート後:{}".format(num))    
