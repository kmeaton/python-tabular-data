#! /usr/bin/env python3

"A module to create scatterplots of sepal length vs. petal length in a plant of interest."

import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def plot_petal_sepal_length(csv, spp, outfile):
    """
    Creates a dataframe containing sepal length, sepal width, petal length, petal width, and species from a csv file of interest.

    Then, creates a plot of sepal length vs. petal length, with a linear regression line.
    
    Parameters
    ----------
    csv : str
        The name of the input csv file, in quotes.

    spp : str
        The name of the species for which you want to isolate records.

    outfile : str
        The desired name of the output png file to which the plot will be written, in quotes.

    Returns
    -------
    None
        Writes plot to outfile.
    """
    input = pd.read_csv(csv)
    dataframe = input[input.species == spp]
    x = dataframe.petal_length_cm
    y = dataframe.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = "Fitted line")
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig(outfile)
    plt.close()
    return None

if __name__ == '__main__':
    plot_petal_sepal_length("iris.csv", "Iris_setosa", "Iris_setosa.png")
    plot_petal_sepal_length("iris.csv", "Iris_versicolor", "Iris_versicolor.png")
    plot_petal_sepal_length("iris.csv", "Iris_virginica", "Iris_virginica.png")
        
