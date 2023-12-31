import pandas as pd
import matplotlib.pyplot as plt


file_path = 'polar_ice_levels.csv'


df = pd.read_csv(file_path, delimiter=',', skipinitialspace=True)
df = df.drop(columns=df.columns[2:])
df = df.loc[3612:6473:365]

sqkm_to_sqmiles = 0.239913
df['Northern_Hemisphere'] = df['Northern_Hemisphere'] * sqkm_to_sqmiles

plt.xticks(df['Date'], ['2016','2017','2018','2019','2020','2021', '2022', '2023'])

plt.plot(df['Date'], df['Northern_Hemisphere'], label = 'Northern_Hemisphere')

plt.title('Ice Levels In The Northern Hemisphere')
plt.ylabel('Square miles of ice')
plt.show()
