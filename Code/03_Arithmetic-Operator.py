import pandas as pd

d1 = pd.DataFrame({'a': [10, 20, 30, 40, 50], 'b':[1,2,3,4,5]})
print(d1)

print("-----------------------------------------------------------")

print("SUM")
d1['sum'] = d1['a'] + d1['b']
print(d1)

print("-----------------------------------------------------------")

print("SUB")
d1['sub']=d1['a'] - d1['b']
print(d1)

print("-----------------------------------------------------------")

print("MUL")
d1['mul']=d1['a'] * d1['b']
print(d1)

print("-----------------------------------------------------------")

print("DIV")
d1['DIV']=d1['a'] / d1['b']
print(d1)

print("-----------------------------------------------------------")

print("GREATER")
d1['greater']= d1['sum'] > 30
print(d1)

print("-----------------------------------------------------------")

print("SMALLER")
d1['smaller']= (d1['mul'] < 100)
print(d1)
