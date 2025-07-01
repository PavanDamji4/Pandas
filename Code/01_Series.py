import pandas as pd

# Creating Series using list
l = [1,2,3,4,5,6,7,8,9,10]
s1 = pd.Series(l)
print(type(s1))
print(s1)

print("-----------------------------------------------------------")

# Series using Dictionaries
d = {'one': [1,2,3], 'two':[4,5,6],'three':[7,8,9]}
s2 = pd.Series(d)
print(s2)

print("-----------------------------------------------------------")

# Directly creating Series
s3 = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'],dtype=float,name="Series3")
print(s3)


print("-----------------------------------------------------------")

# Addtion of 2 Series

s4 = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'],name='Series 1')
s5 = pd.Series([1,2,3],index=['a','b','c'],name='Series 2')
print(s4+s5)

