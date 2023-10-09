import pandas as pd

df = pd.read_excel('wig20_daily.xlsx')

openprice = df['Otwarcie']
date = df['Data']

date1 = date.dt.strftime('%Y-%m-%d')

data_dict = {date1[i]: openprice[i] for i in range(len(openprice))}

print(data_dict)