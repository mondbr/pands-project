# analysis.py
# author: Monika Dabrowska


# this program should:
# 1. Download the data set 
# 2. Outputs a summary of each variable to a single text file
# 3. Saves a histogram of each variable to png files
# 4. Outputs a scatter plot of each pair of variables.
# 5. Performs any other analysis you think is appropriate


# importing nessesary libraries

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

# importing seaborn library for statistical plotting library for Python.
# https://github.com/mwaskom/seaborn
import seaborn as sns


# downloading the data set
# downloading the Iris online dataset (raw file)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# creating a dataframe selecting specific columns to be included in new data frame
# this will be needed in some statistical analysis
# https://www.w3schools.com/python/pandas/pandas_dataframes.asp#:~:text=What%20is%20a%20DataFrame%3F,table%20with%20rows%20and%20columns.
num_df = pd.DataFrame(df, columns=[
                       'sepal_length','sepal_width','petal_length','petal_width'])


# to ignore warnings regarding a change in the figure layout in seaborn:
# https://docs.python.org/3/library/warnings.html
import warnings
warnings.filterwarnings('ignore')


# saving a reference to the original standard output
# will need this to redirecting the standard output (stdout) to a file
# and then to retun to the original output to the terminal
# sys.stdout: https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print
original_stdout = sys.stdout


# creating functions to split the code to separate parts: 

# creating a function that measures the correlation
# will be used few times in the code later:
def iris_correlation():
        
    # assigning data into numpy arrays. 
        s_len = df['sepal_length'].to_numpy()
        s_wth = df['sepal_width'].to_numpy()
        p_len = df['petal_length'].to_numpy()
        p_wth = df['petal_width'].to_numpy()

        # returning the values from a function so can be called out later and assigned to variables
        return s_len, s_wth, p_len, p_wth


# creating a function that will be printing the output to the text file
# this will show a summary of each variable into a single text file
def summary_file():

    # creating a variable and assign a value to it - in this case a text file
    FILENAME = 'summary_analysis.txt'

    
    # using the stdout to redirect the standard output to a file
    # creating (if not already), opening the file with open()
    # w + t:  write/edit (w) mode, text (t) mode
    # assigning the opened file to sys.stdout, that redirects all output that would normally go to the terminal, but will go to the specified file.
    sys.stdout = open (FILENAME, 'w+t') 

    # creating a nice looking formatted text in text file
    # creating a title
    print('\n')
    print('-------------------------------------')
    print(' ### SUMMARY OF THE IRIS DATASET ###')
    print('-------------------------------------')
    print ('\n')

    # writing to the text file an overview of dataset using df()
    print ('Overview of the Iris dataset - First five and last five rows:')
    print ('==============================================================================')
    print(df)
    print ('\n\n')

    # writing to the text file a describe() module for basic statistical values
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
    # creating an another, inside function as it will be apllying to 4 same variables (to simplify and short the code)
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

            #Printing out the summary statistics for variables in the text file
            print(f'\nSummary statistics for {var}:')
            print('--------------------------------------')
            print('Mean: ', mean)
            print('Standard Deviation: ', std_dev)
            print('Minimum: ', minimum)
            print('Maximum: ', maximum)


    # creating list of variable names for summary stats
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


    
    # writing to the text file the output of few other statistical values using dataframe num_df() with numerical variables only
    # writing to the text file  a var() module for info about variance in a Matrix
    print('Dataset Variance:')
    print('=============================================================')
    print(num_df.var())
    print ('\n\n')

    # writing to the text file  a corr() module for info about correlation in a Matrix
    print('Dataset Correlation:')
    print('The closer the value is to 1 the closer the data points fall to a straight line, so the linear association is stronger')
    print('=============================================================')
    print(num_df.corr())
    print ('\n\n')
    
    # writing to the text file  a cov() module for info about covariance in a Matrix
    print('Dataset Covariance Matrix Of Values')
    print('=============================================================')
    print(num_df.cov())
    print ('\n\n')
    

    # Check for NaN values (values with no data)
    # In order to do some statistical calculations, we should not have NaN (no data) values in our dataset. 
    # I learnt about this from similar analysis done by *Sunil Kumar Dash* on [analyticsvidhya.com]
    # (https://www.analyticsvidhya.com/blog/2022/04/data-exploration-and-visualisation-using-palmer-penguins-dataset/).
    # Also I did the same excercise in my other project # https://github.com/mondbr/pofda-mywork
    #  More information of how to delete the NaN data I found on
    # [www.medium.com](https://medium.com/@TheDataScience-ProF/nan-removal-with-python-3d97b954d16d#:~:text=Removing%20NaN%20values%20from%20a%20list%20in%20Python%20can%20be,remove%20them%20from%20a%20list.)
    # and [*ashbabkhan12*](https://ashbabkhan12.medium.com/how-to-remove-nan-values-in-data-using-python-8f959e3d5fbc) blog. 

    print('Number of NaN (no data) values' )
    print('=============================================================')
    
    # Check for NaN values using isna() module
    nan_values = df.isna()

    # Count the number of NaN values in each column
    nan_count_per_column = nan_values.sum()

    # Count the total number of NaN values in the entire DataFrame
    total_nan_count = nan_count_per_column.sum()

    # Print the results
    print('NaN values per column:')
    print(nan_count_per_column)
    print(f'\nTotal NaN values:{(total_nan_count)}')
    print ('\n\n')

    # checking the number of NaN values and return the specific output based of the number of NaNs. 
    if total_nan_count == 0:
        print ('\n\n')
        print('There is no NaN values in this dataset! We can now do the analysis : ) ')
        print ('\n\n')

    else:
        print ('\n\n')
        print('Ups, it seem to be some NaN values, perhaps you need to correct that?')
        print ('\n\n')


    # checking the correlation
    # assigning arrays from iris_correlation() funkction to its corresponding variable so we can use it
    s_len, s_wth, p_len, p_wth = iris_correlation()

    # i learnt about the correlation in python in a ATU module 'Principles in Data Analytics 23/24'
    corr = np.corrcoef([s_len, s_wth, p_len, p_wth])

    # writing to the text file the output of the correlation array
    print('Correlation array')
    print('=============================================================')
    print(corr)
    print ('\n\n')

    
    # finishing the input in the file
    print('\n')
    print('-------------------------------------')
    print(' ### END ###')
    print('-------------------------------------')
    print ('\n')


# Creating a barchart to start my data visualisation
# creating a function that will be creating a bar chart for Iris dataset and save to png file in the repository
def iris_barchart():

    # Setting the variable and using value counts to count them.
    sp_counts = df['species'].value_counts() 

    # Creating the bar chart
    plt.figure(figsize=(8, 5))  # Adjusting the figure size
    # plotting the bar 
    plt.bar(sp_counts.index, sp_counts.values)

    # Adding titles:
    plt.title('Figure 1. Number of Iris flowers of each species', size = 10) # Adjusting the text size
    plt.xlabel('Species', size = 10) # Adjusting the text size
    plt.ylabel('Count', size = 10) # Adjusting the text size



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


def data_hist():
    # Creates a histogram of sepal length all species
    plt.hist(df['sepal_length'], bins=8, color='skyblue', edgecolor='black', density=True)
    plt.title('Figure 2. Histogram of Sepal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    # Plotting density curve
    sns.kdeplot(df['sepal_length'], color='red')
    plt.savefig('2_histogram_of_sepal_length')
    plt.show()

# Creates a histogram of sepal width for all species
    plt.hist(df['sepal_width'], bins=8, color='skyblue', edgecolor='black', density=True)
    plt.title('Figure 3. Histogram of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    # Plottting density curve
    sns.kdeplot(df['sepal_width'], color='red')
    plt.savefig('3_histogram_of_sepal_width')
    plt.show()

# Creates a histogram of petal length for all species
    plt.hist(df['petal_length'], bins=8, color='skyblue', edgecolor='black', density=True)
    plt.title('Figure 4. Histogram of Petal Length')
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Frequency')
    # Plotting density curve
    sns.kdeplot(df['petal_length'], color='red')
    plt.savefig('4_histogram_of_petal_length')
    plt.show()

# Creates a histogram of petal width for all species
    plt.hist(df['petal_width'], bins=8, color='skyblue', edgecolor='black', density=True)
    plt.title('Figure 5. Histogram of Petal Width')
    plt.xlabel('Petal Width (cm)')
    plt.ylabel('Frequency')
    # Plotting density curve
    sns.kdeplot(df['petal_width'], color='red')
    plt.savefig('5_histogram_of_petal_width')
    plt.show()


# creating a function that will create and save a histogram of each variable to png files in this repository
# plotting histogram for each variable
def iris_histograms():
    
    # https://www.kaggle.com/code/alexisbcook/distributions/tutorial
    # setting colors 
    # https://stackoverflow.com/questions/46087192/how-to-set-all-edgecolor-to-none-in-seaborn-matplotlib
    # colors names: https://matplotlib.org/stable/gallery/color/named_colors.html
    # https://seaborn.pydata.org/tutorial/color_palettes.html


    # Creating a separate histogram for  1rd variable Sepal Length for each species using seaborn 
    # I learnt about this in the ATU module 'Principles of Data Analytics' 23/24
    sns.histplot(data=df, x='sepal_length', hue='species', palette='Set2', edgecolor='none') 

    # Add title
    plt.title('Figure 6. Histogram of Sepal Length for Each Species', size = 10)

    # Saving the plot in the repository
    plt.savefig('6_sepal_length_histogram_species.png')

    # checking how the plot look
    plt.show()




    # Creating a separate histogram for 2nd variable Sepal Width for each species using seaborn 
    sns.histplot(data=df, x='sepal_width', hue='species', palette='Set1', edgecolor='none')

    # Add title
    plt.title('Figure 7. Histogram of Sepal Width for Each Species', size = 10)


    # Saving the plot in the repository
    plt.savefig('7_sepal_width_histogram_species.png')

    plt.show()


    # Plotting two other histograms differently using matplotlib.pyplot
    # I learnt about this in the ATU module 'Principles of Data Analytics' 23/24

    # Grouping the data by species
    # https://realpython.com/pandas-groupby/
    # grouped df()
    # https://python.plainenglish.io/preprocessing-and-manipulating-data-for-data-science-using-pandas-721eb2b5a9d7
    grouped_df = df.groupby('species')


    # Creating a separate histogram for each species for 3rd variable Petal Lenght
    plt.figure(figsize=(10, 6))
    for species, data in grouped_df:
        plt.hist(data['petal_length'], bins=10, alpha=0.5, label=species) # alpha parameter sets the transparency level of the plotted points to 50%. It means that the points will be semi-transparent.

    # Add labels and title
    plt.xlabel('Petal Length (cm)', size = 10)
    plt.ylabel('Frequency', size = 10)
    plt.title('Figure 8. Histogram of Petal Length for Each Species', size = 10)
    plt.legend()

    # Save the plot in the repository
    plt.savefig('8_petal_length_histogram_species.png')

    # Show the plot
    plt.show()




    # Creating a separate histogram for each species for 4rd variable Petal Width
    plt.figure(figsize=(10, 6))
    for species, data in grouped_df:
        plt.hist(data['petal_width'], bins=5, alpha=0.5, label=species)

    # Adding labels and title
    plt.xlabel('Petal Width (cm)', size = 10)
    plt.ylabel('Frequency', size = 10)
    plt.title('Figure 9. Histogram of Petal Width for Each Species', size = 10)
    plt.legend()

    # Saving the plot in the repository
    plt.savefig('9_petal_width_histogram_species.png')

    # checking how the plot look
    plt.show()


# creating a function that will create and save scatterplot for each variable to png files in this repository
# plotting a scatterplot ffor each variable
def iris_scatterplots():

    # plotting a scatterplot for sepal and width:
    #setting x-axis variable
    x_var_s = 'sepal_length'

    #setting y-axis variable 
    y_var_s = 'sepal_width' 

    # Create a scatter plot with species showed in different color 
    plt.figure(figsize = (8,6))
    sns.scatterplot(x = x_var_s, y = y_var_s, data = df, marker = 'o', hue = 'species', palette = ['blueviolet','navy','fuchsia']) #marker style to circles #hue to specify variable and set different color to each spiecies

    # Adding labels and titles
    plt.xlabel('Sepal length (cm)', size = 10)
    plt.ylabel('Sepal width (cm)', size = 10)
    plt.title('Figure 10. Sepal length and Sepal width comparison', size = 10)
    plt.legend()
    plt.savefig('10_sepal-length-width_scatt.png')
    plt.show()


    #plotting a scatterplot for petal length and width:
    #setting x-axis variable
    x_var_p = 'petal_length'

    #setting y-axis variable 
    y_var_p = 'petal_width' 

    # Create a scatter plot with species showed in different color 
    plt.figure(figsize = (8,6))
    sns.scatterplot(x = x_var_p, y = y_var_p, data = df, marker = 's', hue = 'species', palette = ['violet','mediumorchid','blue'], edgecolor = 'black')

    # Adding labels and titles
    plt.xlabel('Petal length (cm)', size = 10)
    plt.ylabel('Petal width (cm)', size = 10)
    plt.title('Figure 11. Petal length and Petal width comparison', size = 10)
    plt.legend()
    plt.savefig('11_petal-length-width_scatt.png')
    plt.show()


# creating a function that will create and save a pairplot for each pair of variables to png files in this repository
# plotting a pairplot for each pair of variables
def iris_pairplot():

    # pairwise scatter plot: 
    numeric_vars = ['sepal_length','sepal_width', 'petal_length', 'petal_width']  # adding numeric variable names

    # Creating a scatter plot matrix with color encoding for categorical variables
    # https://stackoverflow.com/questions/43567309/how-to-add-edgecolor-for-the-hist-plot-sons
    sns.pairplot(df, vars=numeric_vars, hue='species', palette = ['fuchsia','mediumorchid','blue'], plot_kws={'edgecolor':'white'}, height=2)
    plt.suptitle('Figure 12. Pairplot Matrix (cm)')  # Add title for the pairplot
    plt.savefig('12_pairwise_scatter_plot.png')

    # Adjusting layout to prevent overlapping labels  
    #https://stackoverflow.com/questions/9603230/how-to-use-matplotlib-tight-layout-with-figure
    plt.tight_layout() 

    # Adjusting layout to prevent overlapping labels
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
    plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, hspace=0.4, wspace=0.4)
    plt.show()


# creating a function that will create and save a scatterplot with a best fit line
# will be needed for measuring the correlation
# Measuring the correlation:
def iris_linespace():

    # assigning arrays from iris_correlation() function to its corresponding variable so we can use it
    # from the correlation array, the strongest positive correlation is between petal lenght and width, so will be adding a best fit line for those two pairs of var.
    s_len, s_wth, p_len, p_wth = iris_correlation()
    

    # The best fit line or optimal relationship can be achieved by minimizing the distances of the data points from the purposed line.
    # I learnt about this in ATU module 'Principles of Data Analytics 23/24
    # A linear equation represents a line mathematically. The normal equation of the line is as follows:
    m, c = np.polyfit(p_len, p_wth, 1)

    # Create x values for best fit line (instead of using values from the dataset)
    bf_x = np.linspace(0, p_len.max()+1, 10) # takes 3 values starting from 0 ending at petal lenght value +1 , giving 8 values equally spaced between those two values. 

    # setting y-axis
    bf_y = m * bf_x + c

    fig, ax = plt.subplots()

    # Plot the  set of data
    ax.plot(p_len, p_wth, 'x', color='blue', alpha=0.5) # alpha parameter sets the transparency level
    ax.plot(bf_x, bf_y , '-r') # 3rd parameter plot line as red color 

    # Adding labels and titles
    ax.set_xlabel('Petal Length (cm)')
    ax.set_ylabel('Petal Width (cm)')
    ax.set_title('Figure 13. Best fit line - Petal length vs Petal Width')

    plt.savefig('13_best_fit_line_petal.png')
    plt.show()

   
# creating a function that will create and save a heatmap that will visualise the correlation
# creating a correlation matrix
def iris_heatmap():

    # To create a heatmap I will use seaborn library based on:
    #https://blog.quantinsti.com/creating-heatmap-using-python-seaborn/

    # assigning arrays from iris_correlation() function
    s_len, s_wth, p_len, p_wth = iris_correlation()

    # creating new array from the variables
    corr_data = np.array([s_len, s_wth, p_len, p_wth])

    # calculating the correlation coefficient matrix
    corr_coef_matrix = np.corrcoef(corr_data)

    # Creating a heatmap
    plt.figure(figsize=(7, 6))
    heatmap = sns.heatmap(corr_coef_matrix, annot=True, cmap='PuRd', fmt='.2f', # cmap color was taken from here: https://matplotlib.org/stable/users/explain/colors/colormaps.html
                xticklabels=['sepal_length (cm)', 'sepal_width (cm)', 'petal_length(cm)', 'petal_width(cm)'], 
                yticklabels=['sepal_length (cm)', 'sepal_width (cm)', 'petal_length(cm)', 'petal_width(cm)'])

    # Add titles and labels
    plt.title('Figure 14. Correlation Coefficient Matrix')
    plt.xlabel('Iris Attributes', fontsize=14) # Set x label font size
    plt.ylabel('Iris Attributes', fontsize=14) # Set y label font size
    plt.xticks  # Rotate x-axis labels for better readability
    plt.yticks # Rotate y-axis labels for better readability

    # Adjust layout to prevent overlapping labels  
    plt.tight_layout() 


    # Set font size for tick labels
    heatmap.tick_params(axis='x', labelsize=8)  # Set x tick label font size
    heatmap.tick_params(axis='y', labelsize=8)  # Set y tick label font size


    plt.savefig('14_correlation_matrix.png')
    plt.show()


# Main code: calling out functions:

iris_correlation()

summary_file()

iris_barchart()

data_hist()

iris_histograms()

iris_scatterplots()

iris_pairplot()

iris_linespace()

iris_heatmap()




# Restore the original standard output
sys.stdout = original_stdout

print('END')