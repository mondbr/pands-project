# analysis.py
# author: Monika Dabrowska


# this program should:
# 1. Download the data set 
# 2. Outputs a summary of each variable to a single text file
# 3. Saves a histogram of each variable to png files
# 4. Outputs a scatter plot of each pair of variables.
# 5. Performs any other analysis you think is appropriate


# Importing nessesary libraries:

## importing pandas to allow us to investigate CSV files and other data exploration
import pandas as pd

## importing sys module
## it gives access to various system-related functionalities, for example to interact with files
## https://www.geeksforgeeks.org/python-sys-module/

import sys


# Downloading the Iris online dataset (raw file)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Checking the output of the dataset
print(df)

# Checking the types of variables in dataset
print (df.info())

# Output a summary of each variable to a single text file
# idea for sys.stdout: https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print

FILENAME = 'summary_analysis.txt'
sys.stdout = open (FILENAME, 'w+t')
print('\n')
print('-------------------------------------')
print(' ### SUMMARY OF THE IRIS DATASET ###')
print('-------------------------------------')
print ('\n')
print ('Overview of the Iris dataset:')
print ('==============================================================================')
print(df)
print ('\n\n')
print('Iris dataset basic statistical values:')
print('=============================================================')
print(df.describe())
print ('\n\n')
print('Number of samples of each type and variable type:')
print('=============================================================')
print(df.info())
print ('\n\n')

























'''
## Render a DataFrame to a console-friendly tabular output:
## https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html
dscr = df.describe().to_string()
sum = df.to_string()
##https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html



# creating a file
FILENAME = 'summary_analysis.txt'
with open(FILENAME, 'w+t') as f:
    f.write('\n')
    f.write('### SUMMARY OF THE IRIS DATASET ###\n')
    f.write(sum)
    f.write('\n')
    f.write('Iris dataset basic statistical values:\n')
    f.write('=============================================================')
    f.write('\n')
    f.write(dscr)
    f.write('\n')
    f.write('=============================================================')
    f.write('\n\n')
    f.write('Number of samples of each type and variable type:\n')
    f.write('=============================================================')
    f.write('\n')
                   # how to save output from dataframe info to text file
    df.info(buf=f) # https://stackoverflow.com/questions/35436331/how-to-save-output-from-dataframe-info-to-file-a-excel-or-text-file
    f.write('=============================================================')
    f.write('\n\n')
'''



