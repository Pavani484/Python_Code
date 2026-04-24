import pandas as pd
data={
    'name':['pavani','lalli','pavana','cherry'],
    'age':[20,23,25,26],
    'marks':[40,45,46,47]
}
df=pd.DataFrame(data)
print(df[['name','marks']])
print(df[df['age']>22])
print(df[df['marks']>43])

print(df[(df['age'] > 21) & (df['marks'] >= 45)])
print(df[(df['age']>=25) & (df['marks']>45)])