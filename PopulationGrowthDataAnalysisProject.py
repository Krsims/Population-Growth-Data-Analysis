import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

df = pd.read_csv('countries.csv')
countries = df

y1952 = countries.loc[countries['year'] == 1952]
y2007 = countries.loc[countries['year'] == 2007]

pop_growth = pd.merge(y1952, y2007, left_on = 'country', right_on = 'country')
pop_growth.drop(columns = ['year_x', 'year_y'], inplace = True)
pop_growth.rename(columns = {'population_x': 'Population 1952', 'population_y': 'Population 2007', 'country': 'Country'}, inplace = True)

pop_growth["Population Growth"] = pop_growth['Population 2007'] - pop_growth['Population 1952']
pop_growth = pop_growth.sort_values('Population Growth', ascending = False)
pop_growth = pop_growth.reset_index()
pop_growth.drop(columns = ['index'], inplace = True)
pop_growth.drop(pop_growth.index[10: ], inplace = True)

Top_Countries = ['China', 'India', 'USA', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', ' Mexico', 'Philippines']
pop_growth = pop_growth['Population Growth'] / 10**6

plt.figure(figsize = (10, 10))
plt.pie(pop_growth, labels = Top_Countries, startangle = 90, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black'})
plt.title('Humans Added Globally by the Top 10 Countries Over 55 Years (1952 - 2007)')
plt.tight_layout()
plt.show()

plt.bar(Top_Countries, pop_growth, edgecolor = 'black', color = ['orange', 'green', 'red', 'yellow', 'blue', 'purple','pink', 'white', 'cyan', 'beige'] )
plt.title('Countries With Largest Population Growth From 1952 - 2007')
plt.ylabel('Population Growth (Millions)')
plt.xticks(rotation = 45)

for x, y in zip(Top_Countries, pop_growth):

    label = '{:.2f}'.format(y)

    plt.annotate(label, (x, y), textcoords = 'offset points', xytext = (0, 10), ha = 'center')

plt.show()

rates = {'China': 13.8622, 'India': 13.4255, 'USA': 2.6107, 'Indonesia': 2.5727, 'Brazil': 2.4256, 'Pakistan': 2.3258, 'Bangladesh': 1.8829, 'Nigeria': 1.8529, 'Mexico': 1.4284, 'Philippines': 1.2480}


cinput = input("Type a top ten country: ")
print('You chose: ', cinput)

year = float(input("How many years from 1952? "))
print(int(year),'years from now is', int(year + 1952))

Prediction = (year * rates.get(cinput))
print('Based on the average population growth per year from 1952 to 2007; in year', int(year + 1952), ' the population of', cinput, 'will be', Prediction, 'million people or', Prediction/10**3, 'billion people.')
