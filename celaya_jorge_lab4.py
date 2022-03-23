"""
Jorge Celaya
NCC CSCE 364; Spring 2022
Lab  #4; celaya_jorge_lab3.py

Code Summary:
"""

import pandas as pd

# meaningful numerical columns: amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest


def getRange(df, column):
    max = round(df[column].max(), 2)
    min = round(df[column].min(), 2)
    return max, min


def getStats(df, column):
    sum = round(df[column].sum(), 2)
    avg = round(df[column].mean(), 2)
    return sum, avg


# As { x } increases,  { y } moves with it
def getCorrelative(df, column):
    pass


# The rate of increase, decrease is moving towards a max/min
def getPrediction(df, column):
    pass


def main():
    df = pd.read_csv("Fraud.csv")

    # TODO: add user interactivity
    max, min = getRange(df, "amount")
    sum, avg = getStats(df, "amount")

    return


main()
