import pandas as pd
import matplotlib.pyplot as plt 

#Nude dataframe
df = pd.read_csv('t1.csv')
df['year'] = pd.DatetimeIndex(df['date']).year

#Wise dataframe
df2 = pd.read_csv('w2.csv')
df2['year'] = pd.DatetimeIndex(df2['date']).year

#Keep years counts on a new dataframe: compare
compare_list = []
compare = pd.DataFrame(compare_list, columns=['nude', 'wise'])
compare['nude'] = df['year'].value_counts()
compare['wise'] = df2['year'].value_counts()
compare = compare.sort_index()

sumall = compare.sum(axis=1)

compareall = compare.copy()

compareall['nude'] = sumall
compareall['wise'] = sumall

forplot = compare / compareall

 
#Make a plot
'''
compare.plot(y=["nude", "wise"], kind="bar")
plt.show()
'''

forplot.plot(
    kind = 'barh',
    stacked = True,
    title = 'Stacked Bar Graph',
    mark_right = True)
plt.show()