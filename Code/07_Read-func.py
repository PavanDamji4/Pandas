import numpy
import pandas as pd

df = pd.read_csv('05_Student Data.csv')

print(df.head(2))
print('--------------------------------------')

print(df.tail(2))
print('--------------------------------------')

print(df.shape)
print('--------------------------------------')

print(df.columns)
print('--------------------------------------')

print(df.dtypes)
print('--------------------------------------')

print(df.info())
print('--------------------------------------')

print(df.describe())
print('--------------------------------------')

print(df[:3])
print('--------------------------------------')

print(numpy.asarray(df))
print('--------------------------------------')

print(df.sort_index())