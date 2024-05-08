# analysis.py
# author: Monika Dabrowska


# this program should:
# Read the dataset 

# Outputs a summary of each variable to a single text file
# Saves a histogram of each variable to png files
# Outputs a scatter plot of each pair of variables.
# Performs any other analysis you think is appropriate


# Importing nessesary libraries:

# importing pandas to allow us to investigate CSV files and other data exploration
import pandas as pd



# Downloading the Iris online dataset (raw file)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")


print(df)





