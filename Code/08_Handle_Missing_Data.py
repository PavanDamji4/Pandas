import pandas as pd

# Sample DataFrame with NaN values
data = {
    'Name': ['Pavan', 'Saurabh', 'Ishwar', None,None],
    'Age': [25, None, 22, 24,None],
    'Marks': [85, 90, None, None,None],
    'City': [None, 'Pune', 'Mumbai', 'Delhi',None]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)
print("-" * 50)

print("Drop rows with any NaN values:\n", df.dropna())
print("-" * 50)

df2 = df.copy()
print("Drop rows where all values are NaN:\n", df2.dropna(how='all'))
print("-" * 50)

print("Drop columns with any NaN values:\n", df.dropna(axis=1))
print("-" * 50)

print("Keep rows with at least 3 non-NaN values:\n", df.dropna(thresh=3))
print("-" * 50)

print("Drop rows where NaN present in 'Marks' or 'City':\n", df.dropna(subset=['Marks', 'City']))
print("-" * 50)

print("Fill NaN with 0:\n", df.fillna(0))
print("-" * 50)

print("Forward fill:\n", df.fillna(method='ffill'))
print("-" * 50)

print("Backward fill:\n", df.fillna(method='bfill'))
print("-" * 50)

print("Fill Age with 30, City with 'Unknown':\n", df.fillna({'Age': 30, 'City': 'Unknown'}))
print("-" * 50)


