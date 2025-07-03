import pandas as pd

d1 = pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10]})
print(d1)

print("-----------------------------------------------------------")

#inserting column

d1.insert(2,'c',[11,12,13,14,15])
print(d1)

print("-----------------------------------------------------------")

# Copying half column to create another column

d1['d'] = d1['c'][:3]
print(d1)

print("-----------------------------------------------------------")

# creating new colum of sum 'a' & 'b'
d1['sum'] = d1['a']+d1['b']
print(d1)

print("-----------------------------------------------------------")

# popping another column
popclm = d1.pop('d')
print(popclm)

print("-----------------------------------------------------------")

print(d1)

print("-----------------------------------------------------------")

del d1['c']
print(d1)

print("-----------------------------------------------------------")

del d1
print(d1)
# successfully deleted the table - so error will be occurred