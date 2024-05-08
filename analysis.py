# analysis.py
# author: Monika Dabrowska


# this program should:
# 1. Download the data set 
# 2. Outputs a summary of each variable to a single text file
# 3. Saves a histogram of each variable to png files
# 4. Outputs a scatter plot of each pair of variables.
# 5. Performs any other analysis you think is appropriate


# Importing nessesary libraries:

# importing pandas to allow us to investigate CSV files and other data exploration
import pandas as pd



# Downloading the Iris online dataset (raw file)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Checking the output of the dataset
print(df)


# Output a summary of each variable to a single text file
## 
FILENAME = 'summary_analysis.txt'
with open(FILENAME, 'w+t') as f:
    for line in f:
        print (line)
    print ("Checking first line")




