import pandas as pd

print("************** one ****************")
df = pd.read_csv("06_Car Data.csv", nrows=20)
print(df)

print("-----------------------------------------------------------")
print("************** two ****************")

df = pd.read_csv("06_Car Data.csv", usecols=['Make', 'Price'])
print(df)

print("-----------------------------------------------------------")
print("************** three ****************")

df = pd.read_csv("06_Car Data.csv", skiprows=5)
print(df)

print("-----------------------------------------------------------")
print("************** four ****************")

df = pd.read_csv("06_Car Data.csv", index_col='Make')
print(df)


print("-----------------------------------------------------------")
print("************** five ****************")

df = pd.read_csv("06_Car Data.csv", dtype={'Price': float})
print(df.dtypes)

print("-----------------------------------------------------------")
print("************** six ****************")

df = pd.read_csv("06_Car Data.csv", na_values=['White'])
print(df)

print("-----------------------------------------------------------")
print("************** seven ****************")


df = pd.read_csv("06_Car Data.csv", header=1)
print(df)