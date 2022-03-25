"""
Jorge Celaya
NCC CSCE 364; Spring 2022
Lab  #4; celaya_jorge_lab3.py

Code Summary: This data set explores the correlation between water temperature and water salinity (salt level).

DATA SET CAN BE DOWNLOADED HERE:
https://www.kaggle.com/sohier/calcofi
EXTRACT 'bottle.csv' FROM DOWNLOADED ZIP FILE
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats


def getOutliers(df, column):
    max = round(df[column].max(), 2)
    min = round(df[column].min(), 2)
    return max, min


def getSummary(df, column):
    sum = round(df[column].sum(), 2)
    avg = round(df[column].mean(), 2)
    return sum, avg


# Is there a relationship between water temperature and salinity?
def getCorrelative(df, x_col, y_col):
    new_df = df[[x_col, y_col]].dropna()  # drop missing values

    x = new_df[x_col]
    y = new_df[y_col]

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    slope = round(slope, 2)
    intercept = round(intercept, 2)

    # graph linear regression line on top of scatter plot
    mpl.rcParams['agg.path.chunksize'] = 10000
    new_df.plot.scatter(x=x_col, y=y_col)  # scatter

    x = np.linspace(28, 37)
    y = x * slope + intercept
    plt.plot(x, y, color="red")  # linear

    plt.title("Water Temperature vs Salinity")
    plt.xlabel("Salinity (g/kg)")
    plt.ylabel("Temperature (deg C)")

    return slope, intercept


# The rate of increase, decrease is moving towards a max/min
def getPredictive(df, slope, intercept):
    max, min = getOutliers(df, "T_degC")
    if slope > 0:
        return max
    elif slope < 0:
        return min
    else:
        return 0


def user_options():
    print("\nThis data set explores the correlation between water salinity (salt level) and water temperature (deg C). ")
    print("\nPlease choose from one of the following.\n")
    print("\t1.) Outliers: Get the high and low values the water salinity.")
    print("\t2.) Summary: Get the sum and average numbers of the water salinity.")
    print("\t3.) Correlative: Get the correlation between water salinity and temperature.")
    print("\t4.) Predictive: Get the rate of increase/decrease and limit of the data set.\n")

    option = input("Please enter which function to run. (enter number): ")

    return option


def main():
    print("Hello, and welcome to lab 4!\n")
    print("Please wait a moment while the data is being processed.")

    df = pd.read_csv("bottle.csv", engine="python")
    slope, intercept = getCorrelative(df, "Salnty", "T_degC")\

    ans = input(
        "Finished processing. Would you like to run a function? (yes/no): ")

    while(ans.lower() == "yes" or ans.lower() == "y"):
        option = user_options()
        print()

        if (option.lower() == "exit" or option.lower() == "quit"):
            break

        try:
            option = int(option)
        except ValueError:
            print("\nThat was not a valid option. Please try again.")

        if option == 1:
            max, min = getOutliers(df, "T_degC")
            print(
                f"The maximum temperature is {max} deg C and the minimum temperature is {min} deg C.")
        elif option == 2:
            sum, avg = getSummary(df, "T_degC")
            print(
                f"The sum of all temperatures is {'{:,.2f}'.format(sum)} deg C and the average temperature is {avg} deg C.")
        elif option == 3:
            if slope > 0:
                print(
                    "As the water salinity increases, the temperature also tends to increase.")
            elif slope < 0:
                print(
                    "As the water salinity increases, the temperature tends to decrease.")
            else:
                print(
                    "As the water salinity increases, the temperature stays roughly constant")
            plt.show()
        elif option == 4:
            lim = getPredictive(df, slope, intercept)
            print(
                f"The rate of change of the water temperature with respect to salinity is roughly {slope} deg C per g/kg of salinity and the temperature moves towards a limit of {lim} deg C.")

        ans = input("\nWould you like to to run another function? (yes/no): ")

    print("\nThank you!")


main()
