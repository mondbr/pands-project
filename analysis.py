# analysis.py
# author: Monika Dabrowska


# this program should:
# 1. Download the data set 
# 2. Outputs a summary of each variable to a single text file
# 3. Saves a histogram of each variable to png files
# 4. Outputs a scatter plot of each pair of variables.
# 5. Performs any other analysis you think is appropriate


### Importing nessesary libraries ###

# importing pandas to allow us to investigate CSV files and other data exploration
import pandas as pd

# importing sys module
# it gives access to various system-related functionalities, for example to interact with files
# https://www.geeksforgeeks.org/python-sys-module/
import sys


# importing the NumPy library and assign as a shorter name 'np'
# NumPy is a Python library used for numercal computing, array manipulation etc.
import numpy as np 

# importing the pyplot module from the Matplotlib library and assigns it an plt.
# module allows creating plots, histograms and adding legends and titles to it.
import matplotlib.pyplot as plt





### Download the data set ###


# Downloading the Iris online dataset (raw file)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Checking the output of the dataset
print(df)

# Checking the types of variables in dataset
print (df.info())



### Output a summary of each variable to a single text file ###


# creating a variable and assign a value to it - in this case a text file
FILENAME = 'summary_analysis.txt'

# sys.stdout: https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print
# redirecting the standard output (stdout) to a file
# creating (if not already) and opening the file with open()
# w + t:  write (w) mode, text (t) mode
# '=' assigns the opened file to sys.stdout, that redirects all output that would normally go to the console to the specified file.
sys.stdout = open (FILENAME, 'w+t') 

#creating a nice looking formatted text in text file
print('\n')
print('-------------------------------------')
print(' ### SUMMARY OF THE IRIS DATASET ###')
print('-------------------------------------')
print ('\n')

# writing to the text file  an overview of dataset using df()
print ('Overview of the Iris dataset:')
print ('==============================================================================')
print(df)
print ('\n\n')

# writing to the text file  a describe() module for basic statistical values
print('Iris dataset basic statistical values:')
print('=============================================================')
print(df.describe())
print ('\n\n')

# writing to the text file  a info() module for info about number of individuals and variable type
print('Number of samples of each type and variable type:')
print('=============================================================')
print(df.info())
print ('\n\n')

# writing to the text file  a info() module for info about number of individuals and variable type
print('Summary of number of each species:')
print('=============================================================')
print(df['species'].value_counts())
print ('\n\n')


# Writing summary statistics for each numerical variable
# Using function as it will be apllying to 4 same variables (to simplify and short the code)
def summary_stats(data, var_names):
    # Iterate over each variable name
    for var in var_names:
        # using describe() module get the basic statistic for variables
        summary = data[var].describe()
    
        # Extracting mean, standard deviation, minimum, and maximum from the summary statistics above
        mean = summary['mean']
        std_dev = summary['std']
        minimum = summary['min']
        maximum = summary['max']

        #Printing out the summary statistics for variables
        print(f'\nSummary statistics for {var}:')
        print('--------------------------------------')
        print('Mean: ', mean)
        print('Standard Deviation: ', std_dev)
        print('Minimum: ', minimum)
        print('Maximum: ', maximum)


# creating list of variable names
variables = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']


# writing to the text file the output of the function created above
print('Summary statistic of each numerical variable:')
print('=============================================================')
print ('\n')
print('What is included in that summary:')
print('_________________________________')
print('Mean: The average value in (cm)')
print('Standard Deviation: Indicates how values are spread out from the mean.')
print('Minimum: The smallest value in the Iris dataset (cm).')
print('Maximum: The largest value in the Iris dataset (cm).' )
print ('\n')
print(f'{summary_stats(df,variables)}')
print ('\n\n')

# Calculating the average value for each variable for each species
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
average_val = df.groupby('species').mean()

# writing to the text file the output of the average above
print('Average value for each variable for each species (cm):')
print('=============================================================')
print(average_val)







### Saving a histogram of each variable to png files in this repository ###

### Creating a barchart for a start


# Setting the variable and using value counts to count them.
sp_counts = df['species'].value_counts() 

# Creating the bar chart
plt.figure(figsize=(8, 5))  # Adjusting the figure size
plt.bar(sp_counts.index, sp_counts.values)

# Adding titles:
plt.title('Figure 1. Number of Iris flowers of each species')
plt.xlabel('Species')
plt.ylabel('Count')



# Adding gridlines for y-axis
# https://www.w3schools.com/python/matplotlib_grid.asp
plt.grid(axis='y')


# Setting y-axis limit to 70 for better visibility
plt.ylim(0, 70)

# Adding specific counts at the top of each bar: 
# Reffering to: https://realpython.com/python-enumerate/
for i, count in enumerate(sp_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Saving the plot in the repository
plt.savefig('1_species_barchart.png')

# checking how the plot look
plt.show()






### plotting histogram for each variable
# colors https://matplotlib.org/stable/gallery/color/named_colors.html

#grouped df()
#https://python.plainenglish.io/preprocessing-and-manipulating-data-for-data-science-using-pandas-721eb2b5a9d7


# Grouping the data by species
grouped_df = df.groupby('species')

# Creating a separate histogram for each species for 1st variable sepal_length
plt.figure(figsize=(10, 6))
for species, data in grouped_df:
    plt.hist(data['sepal_length'], bins=5, alpha=0.5, label=species)

# Adding labels and title
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Figure 2. Histogram of Sepal Length for Each Species')
plt.legend()

# Saving the plot in the repository
plt.savefig('2_sepal_length_histogram_species.png')

# checking how the plot look
plt.show()



# Creating a separate histogram for each species for 2nd variable sepal_width
plt.figure(figsize=(10, 6))
for species, data in grouped_df:
    plt.hist(data['sepal_width'], bins=5, alpha=0.5, label=species)


# Adding labels and title
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.title('Figure 3. Histogram of Sepal Width for Each Species')
plt.legend()

# Saving the plot in the repository
plt.savefig('3_sepal_width_histogram_species.png')

# checking how the plot look
plt.show()




# Creating a separate histogram for each species for 3rd variable Petal Lenght
plt.figure(figsize=(10, 6))
for species, data in grouped_df:
    plt.hist(data['petal_length'], bins=5, alpha=0.5, label=species)

# Add labels and title
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.title('Figure 4. Histogram of Petal Length for Each Species')
plt.legend()

# Save the plot in the repository
plt.savefig('4_petal_length_histogram_species.png')

# Show the plot
plt.show()




# Creating a separate histogram for each species for 4rd variable Petal Width
plt.figure(figsize=(10, 6))
for species, data in grouped_df:
    plt.hist(data['petal_width'], bins=5, alpha=0.5, label=species)

# Define a color palette for each species
colors = {'setosa': 'skyblue', 'versicolor': 'salmon', 'virginica': 'cyan'}

# Adding labels and title
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.title('Figure 5. Histogram of Petal Width for Each Species')
plt.legend()

# Saving the plot in the repository
plt.savefig('5_petal_width_histogram_species.png')

# checking how the plot look
plt.show()





# bins=np.arange(0, 3, 0.15)





'''
# Plotting a histogram for sepal length
plt.hist(df['sepal_length'], bins=20, color='violet', edgecolor='black')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Figure 2. Histogram of Sepal Length')


# Saving the plot in the repository
plt.savefig('sepal_length_histogram.png')

# checking how the plot look
plt.show()


# Plotting a histogram for sepal_width
plt.hist(df['sepal_width'], bins=20, color='plum', edgecolor='black')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.title('Figure 3. Histogram of Sepal Width')


# Saving the plot in the repository
plt.savefig('sepal_width_histogram.png')

# checking how the plot look
plt.show()




# Plotting a histogram for petal_length
plt.hist(df['petal_length'], bins=20, color='aqua', edgecolor='black')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.title('Figure 3. Histogram of Petal Length')


# Save the plot in the repository
plt.savefig('petal_length_histogram.png')

# Saving the plot in the repository
plt.show()



# Plotting a histogram for petal_width
plt.hist(df['petal_width'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.title('Figure 3. Histogram of Petal Width')


# Save the plot in the repository
plt.savefig('petal_width_histogram.png')

# Show the plot
plt.show()


'''













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



