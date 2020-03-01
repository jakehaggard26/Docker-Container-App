#!/usr/bin/env python

# imports
import pandas as pd

if __name__ == '__main__':
    # reads in the csv file
    df = pd.read_csv('pass-2015.csv')
    
    # prints the dimensions of the data frame and displays the name of the columns 
    print("Total Row Number: {0} \nTotal Col Number: {1}".format(df.shape[0], df.shape[1]))
    print(df.columns)
    
    # creates a subset of df to store the player values and qbr
    qbr_data = df[["Player", "Age", "QBR"]]
    
    # drops the null values
    qbr_data = qbr_data.dropna()
    
    # prints the dimensions of the dataframe
    print("Total Row Number: {0} \nTotal Col Number: {1}".format(df.shape[0], df.shape[1]))
    
    # prints the qbr_data data frame
    print("Before: ")
    print(qbr_data)
    
    print()
    
    # sorts the qbr_data data_frame
    qbr_data = qbr_data.sort_values("QBR", ascending=False)
    
    # prints the sorted qbr_data data frame
    print("After: ")
    print(qbr_data)