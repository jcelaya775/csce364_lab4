"""
Jorge Celaya
NCC CSCE 364; Spring 2022
Lab  #4; celaya_jorge_lab3.py

Code Summary:
"""

import pandas as pd
from scipy import stats
from sympy import *

# meaningful numerical columns: amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest


def getOutliers(df, column):
    max = round(df[column].max(), 2)
    min = round(df[column].min(), 2)
    return max, min


def getSummary(df, column):
    sum = round(df[column].sum(), 2)
    avg = round(df[column].mean(), 2)
    return sum, avg


# As { x } increases,  { y } moves with it
# Is there a relationship between water salinity & water temperature?
def getCorrelative(df, x_col, y_col):
    new_df = df[[x_col, y_col]].dropna()

    x = new_df[x_col]
    y = new_df[y_col]

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print(slope, intercept)
    print(f'error: {std_err}')

    return slope, intercept, std_err


# The rate of increase, decrease is moving towards a max/min
def getPredictive(df, x_col, slope, intercept, std_err):
    x = df[x_col]  # make sure that there are no NA values
    expr = slope * x + intercept
    limit_expr = limit(expr, x, 0)

    # search how to do limits w/ python

    return


def user_options():
    print('\nPlease choose from one of the following.\n')
    print('\t1.) Outliers: Get the high and low values the water salinity.')
    print('\t2.) Summary: Get the sum and average numbers of the water salinity.')
    print('\t3.) Correlative: Get the correlation between water salinity and temperature.')
    print('\t4.) Predictive: Get the rate of increase/decrease.\n')

    option = input('Please enter which function to run. (enter number): ')

    return option


def main():
    df = pd.read_csv("bottle.csv", engine="python")

    # max, min = getOutliers(df, "Salnty")
    # sum, avg = getSummary(df, "Salnty")

    slope, intercept, std_err = getCorrelative(df, "Salnty", "T_degC")
    getPredictive(df, slope, intercept, std_err)

    # print('Hello, and welcome to lab 3!\n')
    # ans = input('Would you like to run a function? (yes/no): ')

    # while(ans.lower() == 'yes' or ans.lower() == 'y'):
    #     option = user_options()
    #     print()

    #     if (option.lower() == 'exit' or option.lower() == 'quit'):
    #         break

    #     try:
    #         option = int(option)
    #     except ValueError:
    #         print('\nThat was not a valid option. Please try again.')

    #     if option == 1:
    #         getOutliers(df, "Salnty")
    #     elif option == 2:
    #         getSummary(df, "Salnty")
    #     elif option == 3:
    #         getCorrelative(df, "Salnty", "T_degC")
    #     elif option == 4:
    #         getPredictive(df, "Salnty")

    #     ans = input('\nWould you like to to run another function? (yes/no): ')

    # print('\nThank you!')


main()
