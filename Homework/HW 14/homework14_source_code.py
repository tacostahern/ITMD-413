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
from sklearn import datasets, linear_model

def californiaGraph():
    californiaData = datasets.fetch_california_housing()
    data = pd.DataFrame(californiaData.data, columns= californiaData.feature_names)
    plot = sns.pairplot(data=data, x_vars='Population', y_vars='HouseAge')
    plt.show()

def linearRegression():
    file = pd.read_csv('ave_yearly_temp_nyc_1895-2017.csv')

californiaGraph()