from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv('insurance_age_premium_10k.csv')

ages = df['person_age']
premiums = df['insurance_premium']

# ages = [18,20,21,25,30,35,40]
# conversion in 2d Array, because LinearRegression fit() method needs 2d array
agesForModel = [[x] for x in ages ]
# premiums = [1800,1900,2200,2600,2900,3500,3900]


model = LinearRegression()
model.fit(agesForModel,premiums)

prediction = model.predict([[45]]) 

print(prediction)