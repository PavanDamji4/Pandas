import pandas as pd


# Creating dataframe using dictionary
dic = {'a':[1,2,3,4,5,],'b':[6,7,8,9,10],'c':[11,12,13,14,15],'d':[16,17,18,19,20]}
df1 = pd.DataFrame(dic)
print(df1)
print(type(df1))

print("-----------------------------------------------------------")

#Creating using lists
l = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
df2 = pd.DataFrame(l)
print(df2)

print("-----------------------------------------------------------")

#using custom index and columns and datatypes
l = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
df3 = pd.DataFrame(l,index=[1,2,3,4],columns=['a','b','c','d','e'],dtype=float)
print(df3)

print("-----------------------------------------------------------")

# Using Series
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([6,7,8,9,10])
s3=[s1,s2]
df4 = pd.DataFrame(s3)
print(df4)

print("-----------------------------------------------------------")

# Accessing data from the DataFrame
print(df1['a'][4])
print(df4[4][1])
print(df3['e'][2])

print("-----------------------------------------------------------")

# Printing Custom Columns
print(df2[[0,1]])
