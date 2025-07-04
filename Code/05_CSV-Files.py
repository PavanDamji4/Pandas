import pandas as pd

# firstly creating a DataFrame

df = pd.DataFrame({'Name':['Pavan','Saurabh','Ishwar','Shubham','Shreyash'],'Roll no':[101,102,103,104,105],'ENG':[98,96,94,88,92],'MAR':[80,78,75,79,77],'HIN':[70,69,64,57,67]},index=[1,2,3,4,5])
print(df) # here's the sample dataframe

df.to_csv('05_Student Data.csv',index=False)