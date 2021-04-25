'''
Program Author: Tony Acosta Hernandez
Course: ITMD 413
Program Description: This program will do two things. First, a Seaborn pairplot graph will be created for the
California Housing dataset. Second, a simple linear regression will be done on the ave_yearly_temp_nyc_1895-2017.csv
file.
'''

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def californiaGraph():
    californiaData = datasets.fetch_california_housing()
    data = pd.DataFrame(californiaData.data, columns= californiaData.feature_names)
    plot = sns.pairplot(data=data, x_vars='Population', y_vars='HouseAge')
    plt.show()

def linearRegression():
    nyc = pd.read_csv('ave_yearly_temp_nyc_1895-2017.csv')
    X_train, X_test, y_train, y_test = train_test_split(
        nyc.Date.values.reshape(-1, 1), nyc.Value.values,
        random_state=11)
    
    linear_regression = LinearRegression()
    linear_regression.fit(X=X_train, y=y_train)
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

    predicted = linear_regression.predict(X_test)
    expected = y_test

    predict = (lambda x: linear_regression.coef_ * x + linear_regression.intercept_)

    axes = sns.scatterplot(data=nyc, x='Date', y='Value', hue='Value', palette='winter', legend=False)
    axes.set_ylim(10, 70)

    x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
    y = predict(x)

    line = plt.plot(x, y)

    plt.show() 

californiaGraph()
linearRegression()