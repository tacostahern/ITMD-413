'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will utilize the seaborn library, matplotlib, and several
datasets to create charts that are meant to visualize the data. It will solve the following
problems: 
    a) Using dataset workerstips.csv, create a scatterplot with total_bill as the x-axis and the tips
    as the y-axis.
    b) Using dataset workerstips.csv, create a scatter plot that will differentiate between smokers 
    and non-smokers. Use a different color (hue) and style marker (style) to visually split the 
    points of scatterplot. Because the default range sizes are limited, increase the range size. 
    Try the tuple (10, 300) as the size range parameter.
    c) A simple bar plot will work well to show average tips per day of the week. Find out 
    which day has the highest average tip. In this case, you may want to show the average tip 
    (y-axis) per day of the week (x-axis). 
    d) Repeat part (b) above but this time split the distribution by lunch and dinner. What 
    information can you derive from the new visualization? 
    e) Using dataset flightData.csv, create a lineplot to plot average number of passengers per 
    year per month. Use the year on the x-axis and the passengers on the y-axis. Also, find 
    out how to plot the total number of passengers per year. 
    f) Using dataset titanic.csv, show the counts of observations in each categorical bin using 
    bars plot.
'''
import matplotlib.pyplot as plt, seaborn as sns, pandas as pd

def main():
    workerTips = pd.read_csv('workerstips.csv')
    #Part a answer
    ax = sns.relplot(x = 'total_bill', y = 'tip', data = workerTips)
    ax.set(xlabel = 'Total Bill', ylabel = 'Tips')
    ax.fig.subplots_adjust(top = .95) #For fixing title getting cut off issue
    plt.title('Graph for Part a')
    plt.show()

    #Part b answer
    ax = sns.relplot(x = 'total_bill', y = 'tip', hue = 'smoker', size = 'size', style = 'smoker',  data = workerTips, sizes = (30, 100))
    ax.set(xlabel = 'Total Bill', ylabel = 'Tips')
    ax.fig.subplots_adjust(top = .95) #For fixing title getting cut off issue
    plt.title('Graph for Part b')
    plt.show()

    #Part c answer
    ax = sns.barplot(x = 'day', y = 'tip', data = workerTips, order = ['Thur', 'Fri', 'Sat', 'Sun'])
    ax.set(xlabel = 'Day of the Week', ylabel = 'Average Tips')
    plt.title('Graph for Part c')
    plt.show()

    #Part d answer
    ax = sns.boxplot(x = "day", y = "total_bill", hue = "time", data = workerTips, order = ['Thur', 'Fri', 'Sat', 'Sun'], hue_order = ['Lunch', 'Dinner'])
    ax.set(xlabel = 'Day of the Week', ylabel = 'Average Tips')
    plt.title('Graph for Part d')
    plt.show()
    #The above graph shows us that most of the tips for lunch and dinner are around the same range for Thursday through Friday, with Sunday having the largest distribution of tips.

    #Part e answer
    flightsData = pd.read_csv('flightsData.csv')

    yearlyPassengers = flightsData.groupby('year').sum() #For getting total number of passengers per year
    ax = sns.lineplot(data = flightsData, x = 'year', y = 'passengers')
    ax = sns.lineplot(data = yearlyPassengers, x = 'year', y = 'passengers')
    ax.set(xlabel = 'Year', ylabel = 'Passengers')
    plt.title('Graph for Part e')
    plt.show()

    #Part f answer
    titanicData = sns.load_dataset('titanic')
    ax = sns.catplot(x = 'class', hue = 'who', col = 'survived', data = titanicData, kind = 'count', height = 4, aspect = .7)
    plt.show()
main()