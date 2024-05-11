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


# Importing seaborn library for statistical plotting library for Python.
# https://github.com/mwaskom/seaborn

import seaborn as sns


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

# writing to the text file an info() module for info about individual records and variable type
print('Number of samples of each type and variable type:')
print('=============================================================')
print(df.info())
print ('\n\n')

# writing to the text file  a value counts() module for info about number of each spiecies
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
print ('\n\n')



# Check for NaN values (values with no data)
# In order to do some statistical calculations, I have to remove NaN (no data) values from our dataset. 
# I learnt about this from similar analysis done by *Sunil Kumar Dash* on [analyticsvidhya.com]
# (https://www.analyticsvidhya.com/blog/2022/04/data-exploration-and-visualisation-using-palmer-penguins-dataset/).
#  More information of how to delete the NaN data I found on
# [www.medium.com](https://medium.com/@TheDataScience-ProF/nan-removal-with-python-3d97b954d16d#:~:text=Removing%20NaN%20values%20from%20a%20list%20in%20Python%20can%20be,remove%20them%20from%20a%20list.)
# and [*ashbabkhan12*](https://ashbabkhan12.medium.com/how-to-remove-nan-values-in-data-using-python-8f959e3d5fbc) blog. 

print('Number of NaN (no data) values' )
print('=============================================================')
# Check for NaN values
nan_values = df.isna()

# Count the number of NaN values in each column
nan_count_per_column = nan_values.sum()

# Count the total number of NaN values in the entire DataFrame
total_nan_count = nan_count_per_column.sum()

# Print the results
print('NaN values per column:')
print(nan_count_per_column)
print(f'\nTotal NaN values:{(total_nan_count)}')



### Saving a histogram of each variable to png files in this repository ###




### Creating a barchart for a start


# Setting the variable and using value counts to count them.
sp_counts = df['species'].value_counts() 

# Creating the bar chart
plt.figure(figsize=(8, 5))  # Adjusting the figure size
plt.bar(sp_counts.index, sp_counts.values)

# Adding titles:
plt.title('Figure 1. Number of Iris flowers of each species', size = 10)
plt.xlabel('Species', size = 10)
plt.ylabel('Count', size = 10)



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


# Histograms for each species
# https://www.kaggle.com/code/alexisbcook/distributions/tutorial
# setting colors 
# https://stackoverflow.com/questions/46087192/how-to-set-all-edgecolor-to-none-in-seaborn-matplotlib
# https://seaborn.pydata.org/tutorial/color_palettes.html

sns.histplot(data=df, x='sepal_length', hue='species', palette='Set2', edgecolor='none')

# Add title
plt.title('Figure 2. Histogram of Sepal Length for Each Species', size = 10)

# Saving the plot in the repository
plt.savefig('2_sepal_length_histogram_species.png')

# checking how the plot look
plt.show()





'''
# Creating a separate histogram for each species for 1st variable sepal_length
plt.figure(figsize=(10, 6))
for species, data in grouped_df:
    plt.hist(data['sepal_length'], bins=5, alpha=0.5, label=species)

# Adding labels and title
plt.xlabel('Sepal Length (cm)', size = 10)
plt.ylabel('Frequency', size = 10)
plt.title('Figure 2. Histogram of Sepal Length for Each Species', size = 10)
plt.legend()

# Saving the plot in the repository
plt.savefig('2_sepal_length_histogram_species.png')

# checking how the plot look
plt.show()
'''




# Histograms for each species
# https://www.kaggle.com/code/alexisbcook/distributions/tutorial
sns.histplot(data=df, x='sepal_width', hue='species', palette='Set1', edgecolor='none')

# Add title
plt.title('Figure 3. Histogram of Sepal Width for Each Species', size = 10)


# Saving the plot in the repository
plt.savefig('3_sepal_width_histogram_species.png')

plt.show()

'''

# Creating a separate histogram for each species for 2nd variable sepal_width
plt.figure(figsize=(10, 6))
for species, data in grouped_df:
    plt.hist(data['sepal_width'], bins=5, alpha=0.5, label=species)


# Adding labels and title
plt.xlabel('Sepal Width (cm)', size = 10)
plt.ylabel('Frequency', size = 10)
plt.title('Figure 3. Histogram of Sepal Width for Each Species', size = 10)
plt.legend()

# Saving the plot in the repository
plt.savefig('3_sepal_width_histogram_species.png')

# checking how the plot look
plt.show()

'''

# Plotting two other histograms differently 
# Grouping the data by species
# https://realpython.com/pandas-groupby/

grouped_df = df.groupby('species')


# Creating a separate histogram for each species for 3rd variable Petal Lenght
plt.figure(figsize=(10, 6))
for species, data in grouped_df:
    plt.hist(data['petal_length'], bins=5, alpha=0.5, label=species)

# Add labels and title
plt.xlabel('Petal Length (cm)', size = 10)
plt.ylabel('Frequency', size = 10)
plt.title('Figure 4. Histogram of Petal Length for Each Species', size = 10)
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


# Adding labels and title
plt.xlabel('Petal Width (cm)', size = 10)
plt.ylabel('Frequency', size = 10)
plt.title('Figure 5. Histogram of Petal Width for Each Species', size = 10)
plt.legend()

# Saving the plot in the repository
plt.savefig('5_petal_width_histogram_species.png')

# checking how the plot look
plt.show()



# plotting a scatterplot for sepal and width:

#setting x-axis variable
x_var_s = 'sepal_length'

#setting y-axis variable 
y_var_s = 'sepal_width' 

# Create a scatter plot with species showed in different color 
plt.figure(figsize = (8,6))

sns.scatterplot(x = x_var_s, y = y_var_s, data = df, marker = 'o', hue = 'species', palette = ['blueviolet','navy','fuchsia'])

# Adding labels and titles
plt.xlabel('Sepal length (cm)', size = 10)
plt.ylabel('Sepal width (cm)', size = 10)
plt.title('Figure 6. Sepal length and Sepal width comparison', size = 10)
plt.legend()
plt.savefig('6_sepal-length-width_scatt.png')
plt.show()








# plotting a scatterplot for petal length and width:

#setting x-axis variable
x_var_p = 'petal_length'

#setting y-axis variable 
y_var_p = 'petal_width' 

# Create a scatter plot with species showed in different color 
plt.figure(figsize = (8,6))

sns.scatterplot(x = x_var_p, y = y_var_p, data = df, marker = 'o', hue = 'species', palette = ['violet','mediumorchid','blue'], edgecolor = 'black')

# Adding labels and titles
plt.xlabel('Petal length (cm)', size = 10)
plt.ylabel('Petal width (cm)', size = 10)
plt.title('Figure 7. Petal length and Petal width comparison', size = 10)
plt.legend()
plt.savefig('7_petal-length-width_scatt.png')
plt.show()



# To ignore warnings regarding a change in the figure layout in seaborn:
# https://docs.python.org/3/library/warnings.html

import warnings
warnings.filterwarnings('ignore')



# pairwise scatter plot: 
numeric_vars = ['sepal_length','sepal_width', 'petal_length', 'petal_width']  # adding numeric variable names


# Create a scatter plot matrix with color encoding for categorical variables
# https://stackoverflow.com/questions/43567309/how-to-add-edgecolor-for-the-hist-plot-sons
sns.pairplot(df, vars=numeric_vars, hue='species', palette = ['fuchsia','mediumorchid','blue'], plot_kws={'edgecolor':'white'}, height=2)
plt.suptitle('Figure 8. Pairwise Scatter Plot Matrix (cm)')  # Add title for thepairplot
plt.savefig('8_pairwise_scatter_plot.png')

# Adjust layout to prevent overlapping labels  
#https://stackoverflow.com/questions/9603230/how-to-use-matplotlib-tight-layout-with-figure
plt.tight_layout() 

#Adjust layout to prevent overlapping labels
plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, hspace=0.4, wspace=0.4)

plt.show()





# Measuring the correlation:


# Let's get the data into numpy arrays. 
s_len = df['sepal_length'].to_numpy()
s_wth = df['sepal_width'].to_numpy()
p_len = df['petal_length'].to_numpy()
p_wth = df['petal_width'].to_numpy()
specs = df['species'].to_numpy()



# Measure the correlation

corr = np.corrcoef([s_len, s_wth, p_len, p_wth])

# writing to the text file the output of the correlation array
print('Correlation array - The closer the value is to 1 the closer the data points fall to a straight line, so the linear association is stronger:')
print('=============================================================')
print(corr)
print ('\n\n')


#The best fit line or optimal relationship can be achieved by minimizing the distances of the data points from the purposed line.
# A linear equation represents a line mathematically. The normal equation of the line is as follows:

m, c = np.polyfit(p_len, p_wth, 1)

print(m, c)



# Create x values for best fit line (instead of using values from the dataset)
bf_x = np.linspace(0, p_len.max()+1, 10) # takes 3 values starting from 0 ending at max body mass value +1 , giving 8 values equally spaced between those two values. 

# setting y-axis
bf_y = m * bf_x + c

fig, ax = plt.subplots()
# Plot the first set of data

ax.plot(p_len, p_wth, 'x', color='blue', alpha=0.5) # alpha parameter sets the transparency level of the plotted points to 50%. It means that the points will be semi-transparent. 

ax.plot(bf_x, bf_y , '-r') # 3rd parameter - plot them as red color 

# Labels
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')

ax.set_title('Figure 9. Best fit line - Petal length vs Petal Width')

plt.savefig('9_best_fit_line_petal.png')
plt.show()


### Figure correlation matrix


# To create a heatmap I will use seaborn library based on:
#https://blog.quantinsti.com/creating-heatmap-using-python-seaborn/

corr_data = np.array([s_len, s_wth, p_len, p_wth])

# Calculate the correlation coefficient matrix
corr_coef_matrix = np.corrcoef(corr_data)

# Create a heatmap
plt.figure(figsize=(7, 6))
heatmap = sns.heatmap(corr_coef_matrix, annot=True, cmap='PuRd', fmt='.2f', # cmap color was taken from here: https://matplotlib.org/stable/users/explain/colors/colormaps.html
            xticklabels=['sepal_length (cm)', 'sepal_width (cm)', 'petal_length(cm)', 'petal_width(cm)'], 
            yticklabels=['sepal_length (cm)', 'sepal_width (cm)', 'petal_length(cm)', 'petal_width(cm)'])

# Add titles and labels
plt.title('Figure 10. Correlation Coefficient Matrix')
plt.xlabel('Iris Attributes', fontsize=14) # Set x label font size
plt.ylabel('Iris Attributes', fontsize=14) # Set y label font size
plt.xticks  # Rotate x-axis labels for better readability
plt.yticks # Rotate y-axis labels for better readability

# Adjust layout to prevent overlapping labels  
plt.tight_layout() 


# Set font size for tick labels
heatmap.tick_params(axis='x', labelsize=8)  # Set x tick label font size
heatmap.tick_params(axis='y', labelsize=8)  # Set y tick label font size


plt.savefig('10_correlation_matrix.png')
plt.show()







# bins=np.arange(0, 3, 0.15)

# sepal_length  sepal_width  petal_length  petal_width    species


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
