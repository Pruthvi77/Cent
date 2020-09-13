import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})

# task 1
for i in range(1, df['FlightNumber'].count() + 1):
    if pd.isnull(df.loc[i, 'FlightNumber']):
        df.loc[i, 'FlightNumber'] = df.loc[i - 1, 'FlightNumber'] + 10
print(df)



print('---------------------------------------------------------------------------------------------------------------')
#task 2
df[['From', 'To']] = df.From_To.str.split("_",expand=True)
print(df)


print('---------------------------------------------------------------------------------------------------------------')
#task 3
df.From =  df.From.str.capitalize()
df.To =  df.To.str.capitalize()
df.From_To =  df.From.str.capitalize()
print(df)

#task 4
print('---------------------------------------------------------------------------------------------------------------')
temp = df.drop('From_To',axis=1)
print(temp)
