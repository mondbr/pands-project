<img src="https://vlegalwaymayo.atu.ie/pluginfile.php/1/theme_catawesome/logo/1708672446/logo.svg" width=20% height=20%>

# Programming and Scripting Project 

by Monika Dabrowska

This repository is for the the assessment project for the Programming and Scripting module in the Higher Diploma in Data Analytics course at [ATU](https://www.atu.ie/) in the summer semester of 2023/24.


## Assessment Overview

This project is about Fisher's Iris flower dataset. 
It is a very popular dataset in data analytics particularly for learning purposes.
It's widely used in statistics, machine learning, data visualization and analysis due to its relatively small size and easy-to-understand structure.

To work on this project I had to do the research of the dataset, write a documentation and use Python code to investigate this data. 
 
The script that outputs the elements for the analysis is submitted in single python file *analysis.py* in this GitHub repository. 

#### [Open here - Python program that outputs the analysis elements - *analysis.py*](https://github.com/mondbr/pands-project/blob/main/analysis.py)


<div style="text-align:center">
<img src="https://img.freepik.com/free-photo/beautiful-fresh-blue-bloom-dew_23-2148069238.jpg?w=740&t=st=1715802277~exp=1715802877~hmac=67c7336b375d7eca3e50cce92747c0d3b8c182b61d70977cf9dda55cbf9fbdef" width=50% height=50%>
<div style="text-align:center"><b>Artwork by www.freepik.com</b>
</div>

## Use of this project 

This project is mainly created for the assessment and educational purposes, but it can be used for further analysis. 

## Get Started

To begin, you need Python installed on your machine. To do that, you can use the following: 

**Anaconda** \
[Download](https://www.anaconda.com/download) \
The easiest way to install Python and the necessary packages for this course.

**Visual Studio Code** \
[Download](https://code.visualstudio.com) \
The editor I will use to create Python scripts. 

**Git** \
[Download](https://git-scm.com) \
The software I will use to track my progress.



## Table of contents - Analysis of Iris Data set

* [About Iris Dataset (History)](#about-iris-dataset-history)
* [Iris Dataset file](#iris-dataset-file)
* [Data set analysis - libraries and code](#data-set-analysis---libraries-and-code)
    * [Imports libraries and modules](#import-libraries-and-modules)
    * [Import Dataset and DataFrame](#import-dataset-and-dataframe)
    * [My functions](#my-functions)
    * [Redirecting summary to the text file](#redirecting-summary-to-the-text-file)
    * [Data visualisation and plots](#data-visualisation-and-plots)
    * [Finalizing the file](#finalizing-the-file)
* [Results](#results)
* [References / Library](#references)


## Data Collection and Methodology:

The iris flowers data was downloaded from [mwaskom/seaborn on Github](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv) and loaded to the *analysis.py* file in this repository. 

You can learn more about Iris dataset on [Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set).

I worked on this project using Python programming and libraries such as Pandas, NumPy, matplotlib, and Seaborn for data analysis and visualization. I also reffered to multiple resourses available online. 
 
# Analysis of the Iris data set

The below section contains an overwiev of my project about analysis of well-known Iris Dataset as part of the assessment project for Programming and Scripting module on Higher Diploma in Data Analytics course from [ATU](https://www.atu.ie/) in Summer 2023/24.

I will explain my approach to the solution of given tasks, my research and references for the code I wrote and results of my analysis. 

The program is written in the file [**analysis.py**](https://github.com/mondbr/pands-project/blob/main/analysis.py) saved in this repository. The file also contains comments to the code I wrote. 

<img src="https://github.com/mondbr/pands-project/blob/main/Species_image.png">
<p style="font-size: 10px;">Photo edit by Monika Dabrowska, photos via Wikipedia</p>



## About Iris Dataset (History)

The *Iris flower dataset*, also known as *Fiher's Iris dataset* is a [multivariate](https://en.wikipedia.org/wiki/Multivariate_statistics) dataset popularized by British statistitian and biologist [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) in his 1936 publication *The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis*. The free access to the full article in PDF in online library can be found [here](https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x). 

In this article, Fisher developed and evaluated a linear function to differentiate Iris species based on the morphology of their flowers. It was the first time that the sepal and petal measures of the three Iris species appeared publicly.

The majority of the data was collected by [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson) to quantify the morphological variation of Iris flowers from three related species - *Iris setosa*, *Iris virginica* and *Iris versicolor*. Two of the three species were collected in the [Gaspé Peninsula](https://en.wikipedia.org/wiki/Gasp%C3%A9_Peninsula) region in Canada, with all samples taken from the same pasture, picked on the same day, and measured by the same person using the same apparatus. This careful collection method ensured consistency and accuracy in the measurements.

The data contains an information of 50 samples from each of three species and its four features - the length and the width of the sepals and petals, in centimeters. 

The Iris data has become a widely used tool for pattern recognition and classification tasks across various fields, including machine learning, analysis, statistics, and biology.

*(source: [wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set))*


Iris flower features are pictured below: 


<img src="https://media.licdn.com/dms/image/D5612AQFvpSLdhkfa0g/article-cover_image-shrink_600_2000/0/1694107215197?e=2147483647&v=beta&t=aSiPQP37OssvFRNT_Gjf95WZfTlr5CB3n_apgLGLrqo" width=30% height=30%>
<p style="font-size: 8px;">Photo from Hani Abudaba on LinkedIn</p>


## Iris Dataset file

The Iris flower dataset contains a set of 150 individual records which represents three Iris speecies:
- Iris Setosa - 50 samples
- Iris Virginica - 50 samples
- Iris Versicolor - 50 samples

The columns represents plant features such as:
- Sepal Lenght in cm
- Sepal Width in cm
- Petal Lenght in cm
- Petal Width in cm

The Iris flowers data was downloaded from [mwaskom/seaborn on Github](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv) and loaded to the [*analysis.py*](https://github.com/mondbr/pands-project/blob/main/analysis.py) file in this repository.

## Data Set Analysis - libraries and code
In this paragraph I will explain the necessary libraries imported that are needed for this analysis, the dataset import and the code to write a script for summary creation.

### Import libraries and modules

    # importing nessesary libraries
        import pandas as pd
        import sys
        import numpy as np 
        import matplotlib.pyplot as plt
        import seaborn as sns

[**pandas**](https://www.w3schools.com/python/pandas/pandas_intro.asp#:~:text=Pandas%20is%20a%20Python%20library,by%20Wes%20McKinney%20in%202008.) is a Python library that is used for workings with datasets. It offers a range of functions for analyzing, cleaning, exploring, and manipulating data. The name "Pandas" references both "Panel Data" and "Python Data Analysis." The library was created by Wes McKinney in 2008.
In this project *pandas* is used for creating a summary of the dataset from a *.csv file. 

[**sys**](https://docs.python.org/3/library/sys.html) module provides access to system-specific parameters and functions, allowing interaction with the Python runtime environment. It can be used to handle command-line arguments, manage the Python interpreter, and control input and output.
In this project *sys* is used to redirect the standard output to a file instead to a terminal/console, as I will be writing the analysis to the text file called [*summary-analysis.txt*](https://github.com/mondbr/pands-project/blob/main/summary_analysis.txt).

[**NumPy**](https://numpy.org/doc/stable/user/absolute_beginners.html) is a fundamental Python library used for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with variety of mathematical functions to operate on these arrays. *NumPy* is widely used in various fields such as mathematics, statistics and data science.
In this project *NumPy* is used to create a numerical arrays and analyse the correlation between numerical variables.

[**myplotlib**](https://matplotlib.org/stable/) and its module [**pyplot**](https://matplotlib.org/stable/api/pyplot_summary.html) allows to work on mathematical calculations, array manipulations, creating plots and histograms. 
In this project *matplotlib.pyplot* is used to plot varoius of histograms and other plots of the Iris data variables.

[**seaborn**](https://seaborn.pydata.org/index.html) is another Python library built on to of Matplotlib. It is used for statistical data visualisation that helps to provide a nicely looking statistcal graphics.
In this project *seaborn* is used for plotting plots and histograms for analysis.



### Import dataset and DataFrame

To work on the summary, I needed to find the data online and load it to my program. 

The below lines of code are used for reading the raw *.csv file available online and put into a DataFrame.

A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

Raw file contains plain text format (Comma-Separated Values) of data that will be used for my analysis. 

    # downloading the Iris online dataset (raw file)
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

The above code loads the data into a DataFrame named *df*. This DataFrame contains all the columns that are in the CSV file. It is ready now to work on it in my analyis. 

To be able to calculate and show statistical summary of numerical columns in some of my code, I created a new DataFrame below named *num_df* from an existing DataFrame *df*. I selected specific columns **'sepal_length', 'sepal_width', 'petal_length', 'petal_width'**, so my new DataFrame contains only these columns. I will need this in execution of a few Python methods in my code.

    # creating a dataframe selecting specific columns to be included in new data frame
    num_df = pd.DataFrame(df, columns=[
                            'sepal_length','sepal_width','petal_length','petal_width'])


During my work on the code in this project and project for another module, I came accross warnings being shown on my terminal. They were related to *change in the figure layout in seaborn*. With discussing this with my ATU collegues and doing research I learnt that I can use below code to simply ignore the messages being prompted. 

This can be used for a cleaner output and no-distraction especially for scripts or notebooks where warnings are not critical and do not affect the results.

However, while ignoring warnings can be helpful in certain situations, it's generally better to address warnings appropriately. Warnings often indicate potential issues in code or data. Ignoring them may hide important information that could tell diagnosing problems or improving quality of the code. 

I was reffering to the information provided on [docs.python](https://docs.python.org/3/library/warnings.html). 


    # to ignore warnings regarding a change in the figure layout in seaborn
    import warnings
    warnings.filterwarnings('ignore')

Now, I will explain my approach to one of the task of this project, where I need to write my summary output to the single .txt file. Initially I wanted to use *open()* function and *write()* method, however I found it difficult to include Python built-in functions such as *describe()* or *info()* etc, because *.write()* function only takes string (text) value as an input. I was reffering to information on [w3schools.com](https://www.w3schools.com/python/ref_file_write.asp).

After further research I learnt that more useful will be using *sys.stdout()* to re-direct the standard output to a file. 
To be able to restore it later and come back to original output I created the below reference.
I was reffering to the below sources available on [geeksforgeeks.com](https://www.geeksforgeeks.org/sys-stdout-write-in-python/) and [stackoverflow.com](https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print). 

    # saving a reference to the original standard output
    original_stdout = sys.stdout


### My functions 

To present my work in more structured way, I organised my code in this file by creating functions to break it for smaller parts for each task that are easier to work on and read.
The knowledge how to do it I learnt throughout the module. 

The list of my functions are presented as follows and they are called out at the end of the file:

- [*iris_correlation()*](#def-iris_correlation)

- [*summary_file()*](#def-summary_file)

    - [*def summary_stats()*](#def-summary_stats)

- [*iris_barchart()*](#def-iris_barchart)

- [*data_hist()*](#def-data_hist)

- [*iris_histograms()*](#def-iris_histograms)

- [*iris_scatterplots()*](#def-iris_scatterplots)

- [*iris_pairplot()*](#def-iris_pairplot)

- [*iris_linespace()*](#def-iris_linespace)

- [*iris_heatmap()*](#def-iris_heatmap)

### Redirecting summary to the text file

#### *def* *iris_correlation()*

My first function (although that was added later while working on the code) is *def iris_correlation():* 
I created this to assign the data into numpy arrays. I will need this later in my summary file, but also to calculate the correlation. 
I was reffering to the following sources: Numpy arrays - ATU modules, [datacamp.com](https://www.datacamp.com/tutorial/python-numpy-tutorial) and [realpython.com](https://realpython.com/python-return-statement/)

The code is: 

    def iris_correlation():
        
    # assigning data into numpy arrays. 
        s_len = df['sepal_length'].to_numpy()
        s_wth = df['sepal_width'].to_numpy()
        p_len = df['petal_length'].to_numpy()
        p_wth = df['petal_width'].to_numpy()

        # returning the values from a function so can be called out later and assigned to variables
        return s_len, s_wth, p_len, p_wth

#### *def* *summary_file()*

This is a function that is printing the output to the text file and provide varoius information about the dataset.

I can use now *sys.stdout()* to set a default place to send a program’s text output and use *print()* function so all the output will be printed and saved in my dedicated .txt file. 

    # creating a variable and assign a value to it - in this case a text file
    FILENAME = 'summary_analysis.txt'

    # using the stdout to redirect the standard output to a file
    sys.stdout = open (FILENAME, 'w+t') 

In my [**analysis.py**](https://github.com/mondbr/pands-project/blob/main/analysis.py) file I can now use varoius of functions and methods to show summary values of the dataset:


- **print(df)** will give us an overview of the Iris dataset. We don't see the full table with entire data, but only a few rows. That does not mean we don't have that information. Rows that are out of screen are reffered as three dots. This way, we can see first five rows and last five rows of the table instead of presenting full table with entire data, but the information is still there.

We run the program:

    $ analysis.py

The program output is: 

    sepal_length  sepal_width  petal_length  petal_width    species
    0             5.1          3.5           1.4          0.2     setosa
    1             4.9          3.0           1.4          0.2     setosa
    2             4.7          3.2           1.3          0.2     setosa
    3             4.6          3.1           1.5          0.2     setosa
    4             5.0          3.6           1.4          0.2     setosa
    ..            ...          ...           ...          ...        ...
    145           6.7          3.0           5.2          2.3  virginica
    146           6.3          2.5           5.0          1.9  virginica
    147           6.5          3.0           5.2          2.0  virginica
    148           6.2          3.4           5.4          2.3  virginica
    149           5.9          3.0           5.1          1.8  virginica


- **print(df.describe())** will give us basic statistical values for each variable: 

The program output is: 

    sepal_length  sepal_width  petal_length  petal_width
    count    150.000000   150.000000    150.000000   150.000000
    mean       5.843333     3.057333      3.758000     1.199333
    std        0.828066     0.435866      1.765298     0.762238
    min        4.300000     2.000000      1.000000     0.100000
    25%        5.100000     2.800000      1.600000     0.300000
    50%        5.800000     3.000000      4.350000     1.300000
    75%        6.400000     3.300000      5.100000     1.800000
    max        7.900000     4.400000      6.900000     2.500000

Where each value states as follows:

    - count - The number of not-empty values.
    - mean - The average (mean) value.
    - std - The standard deviation.
    - min - The minimum value.
    - 25% - The 25% percentile.
    - 50% - The 50% percentile.
    - 75% - The 75% percentile.
    - max - The maximum value.

- **print(df.info())** will give us a number of samples of each type and variable type. 

The program output is: 

    RangeIndex: 150 entries, 0 to 149
    Data columns (total 5 columns):
       Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
    0   sepal_length  150 non-null    float64
    1   sepal_width   150 non-null    float64
    2   petal_length  150 non-null    float64
    3   petal_width   150 non-null    float64
    4   species       150 non-null    object 
    dtypes: float64(4), object(1)
    memory usage: 6.0+ KB
    None



- **print(df['species'].value_counts())** will provide us with the number per selected category, in this case by species. 

The program output is: 

    species
    setosa        50
    versicolor    50
    virginica     50
    Name: count, dtype: int64


I also wanted to get more detailed statistical analysis, for example to display summary for each variable individually. To do this, I decided to create another function, inside the current one, as the same action will be applied to 4 variables. 

##### *def* *summary_stats()*

The code: 

    # Iterate over each variable name
        for var in var_names:

            # using describe() module get the basic statistic for variables
            summary = data[var].describe()
    
            # Extracting mean, standard deviation, minimum, and maximum from the summary statistics above
            mean = summary['mean']
            std_dev = summary['std']
            minimum = summary['min']
            maximum = summary['max']

I started with a *for* loop that go over each element in the list *var names*. Each element represents a variable name from the DataFrame. 
Then, for each variable name in *var_names* the *describe()* method generates a summary statistic for the variable. 
Next, I extracted specific statistics from the summary: mean, standard deviation, min value and max value. 

- **print(f'{summary_stats(df,variables)}')**

After creating list of variable names, and printing out the function created above using *print(f'{summary_stats(df,variables)}')*, the output is as follows:

    Summary statistics for sepal_length:
    --------------------------------------
    Mean:  5.843333333333334
    Standard Deviation:  0.8280661279778629
    Minimum:  4.3
    Maximum:  7.9

    Summary statistics for sepal_width:
    --------------------------------------
    Mean:  3.0573333333333337
    Standard Deviation:  0.435866284936698
    Minimum:  2.0
    Maximum:  4.4

    Summary statistics for petal_length:
    --------------------------------------
    Mean:  3.7580000000000005
    Standard Deviation:  1.7652982332594667 
    Minimum:  1.0
    Maximum:  6.9

    Summary statistics for petal_width:
    --------------------------------------
    Mean:  1.1993333333333336
    Standard Deviation:  0.7622376689603465
    Minimum:  0.1
    Maximum:  2.5

- **print(average_val)**

Then I wanted to see the the average value for each variable for each species. After grouping DataFrame df by the 'species' I calculated the mean of each numerical column for each species group.
I was reffering to information available on [pandas.pydata.org](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)

The output is:

    Average value for each variable for each species (cm):
    =============================================================
        sepal_length  sepal_width  petal_length  petal_width
    species                                                         
    setosa             5.006        3.428         1.462        0.246
    versicolor         5.936        2.770         4.260        1.326
    virginica          6.588        2.974         5.552        2.026



- **print(num_df.var()), print(num_df.corr()), print(num_df.cov())**

I was looking for the informaton how I can print other statistical values such as variance, correlation and covariance. By following the below links I was able to present this information in a Matrix of values:

- [pandas.DataFrame.var](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html)
- [pandas.DataFrame.cov](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.cov.html)
- [pandas.DataFrame.corr](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)

As the default value of *numeric_only* is false, that is why I was getting error while I was using my original DataFrame *df*, since there are string variables (species). 
To fix that problem I decided to create a new DataFrame *num_df* as mentioned in one of the paragraph before, with only numeric variables. However, just adding a condition to original DataFrame *(df.var(numeric_only=True))* would give me the same result. For my educational purposes I decided to keep those two options for future reference. 

The output is:

    Dataset Variance:
    Measures the spread or dispersion of individual data points from the mean
    =============================================================
    sepal_length    0.685694
    sepal_width     0.189979
    petal_length    3.116278
    petal_width     0.581006
    dtype: float64



    Dataset Variance original DataFrame df:
    =============================================================
    sepal_length    0.685694
    sepal_width     0.189979
    petal_length    3.116278
    petal_width     0.581006
    dtype: float64



    Dataset Correlation:
    The closer the value is to 1 the closer the data points fall to a straight line, so the linear association is stronger
    =============================================================
                sepal_length  sepal_width  petal_length  petal_width
    sepal_length      1.000000    -0.117570      0.871754     0.817941
    sepal_width      -0.117570     1.000000     -0.428440    -0.366126
    petal_length      0.871754    -0.428440      1.000000     0.962865
    petal_width       0.817941    -0.366126      0.962865     1.000000



    Dataset Covariance Matrix Of Values
    Measures the extent to which two variables change together, indicating the direction
    =============================================================
                sepal_length  sepal_width  petal_length  petal_width
    sepal_length      0.685694    -0.042434      1.274315     0.516271
    sepal_width      -0.042434     0.189979     -0.329656    -0.121639
    petal_length      1.274315    -0.329656      3.116278     1.295609
    petal_width       0.516271    -0.121639      1.295609     0.581006


- **nan_values = df.isna()**

With having a small experience already with working on another project for ATU assessment, I came across the situation where I could not work on some analysis where I have NaN (no data) values in my data set. 
I decided then to check if there are any NaN values in this dataset just in case that this my impact my correlation analysis I wanted to do later on:
To check that, I ran a script checking the NaN values in dataset, count them and print the output depending on the number of NaN values using *if* statement. If the number would be more than 0, that would mean there are some NaN values and I would need to do additional manipulation on dataset to clear/ignore NaN values. 

I learnt about this from similar analysis done by *Sunil Kumar Dash* on [analyticsvidhya.com](https://www.analyticsvidhya.com/blog/2022/04/data-exploration-and-visualisation-using-palmer-penguins-dataset/). More information of how to delete the NaN data I found on [www.medium.com](https://medium.com/@TheDataScience-ProF/nan-removal-with-python-3d97b954d16d#:~:text=Removing%20NaN%20values%20from%20a%20list%20in%20Python%20can%20be,remove%20them%20from%20a%20list.) and [*ashbabkhan12*](https://ashbabkhan12.medium.com/how-to-remove-nan-values-in-data-using-python-8f959e3d5fbc) blog. 


The output of this script is:

    Number of NaN (no data) values
    =============================================================
    NaN values per column:
    sepal_length    0
    sepal_width     0
    petal_length    0
    petal_width     0
    species         0
    dtype: int64

    Total NaN values:0
    There is no NaN values in this dataset! We can now do the analysis : )


- **print(corr)**

This is another way to check the correlation, this time in numpy array. We were discussing this during the ATU modules. 
I decided to keep this in my **summary_analysis.txt** file as I will need that later in my data visualisation. 
I called a function *iris_correlation()* and assigned four numerical variables that I will neeed. It will return four arrays corresponding to different measurements (such as sepal length, sepal width, petal length, and petal width) from the iris dataset.

Then, by using *np.corrcoef()* function from the NumPy library I calculated the Pearson correlation coefficients between variables to find the relationship between the variables. 

The code is: 

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

The output is:

    Correlation array
    =============================================================
    [[ 1.         -0.11756978  0.87175378  0.81794113]
    [-0.11756978  1.         -0.4284401  -0.36612593]
    [ 0.87175378 -0.4284401   1.          0.96286543]
    [ 0.81794113 -0.36612593  0.96286543  1.        ]]

By the above we can tell that the strongest positive correlation is 0.96 between petal lenght (3<sup>[*st*](https://www.w3schools.com/tags/tag_sup.asp)</sup>) and petal width (4<sup>st</sup>). 

#### **Summary**

In the above code I presented a numerous examples of how to show the summary of the Iris Dataset. I have not only practised of how to work on the dataset, but also how to re-direct the input to be presented in a text file with a good looking, readable format. To tell the user that the file is finished, I added a simple print **END** in the text file.

### Data visualisation and plots

After working on some text descriptions and summaries, in this section I will present my work on visualising the dataset in a barchart, histograms, pairplots scatterplot and heatmap. 
For each of the type I created a separate function that will create a plot, show it to the user and save in the repository as a *.png file. 

#### Barchart and Histograms

##### *def* *iris_barchart()*

Firstly, I wanted to present a bar chart for Iris dataset with a function *def iris_barchart()*: that will show the number of Iris flowers of each species:

The code is: 
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


<div style="text-align: center;">
    <img src="https://github.com/mondbr/pands-project/blob/main/1_species_barchart.png" width=70% height=70%>
</div>

The above visualisation tells us that there is 50 samples of each species.

**Histograms**

##### *def* *data_hist():*

Function *def data_hist():*  creates and saves a histogram of each variable to .png files in this repository. I will present here a code for one of the variable, *sepal_length*, as the code is similar for the other variables, with variable name as the change:

The code is: 

    # Creates a histogram of sepal length all species
    plt.hist(df['sepal_length'], bins=8, color='skyblue', edgecolor='black', density=True)
    plt.title('Figure 2. Histogram of Sepal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    # Plotting density curve
    sns.kdeplot(df['sepal_length'], color='red')
    plt.savefig('2_histogram_of_sepal_length')
    plt.show()


With use of matplotlib.pyplot I plotted the below histograms. Majority of the parameters are set to present the histogram in better looking way:
- *bins* parameter specifies the number of bins or intervals to divide the data into. Here, it's set to 8 bins.
- *color='skyblue*' and *edgecolor='black'* set the color of the bars and their edges
- *density=True* normalizes the histogram so that the area under the histogram equals 1,
- *plt.title, plt.xlabel and plt.ylabel* are setting titles of the histogram

I also decided that I would like to see a line that shows how data is spread out across different values. I was reffering to information available on [seaborn.pydata.org](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) that helped me to create a line to show that shape called a density curve with using seaborn.kdeplot(). 

After that I use the code to save the a *.png file with specific title but also show to the user for a reference. 



<img src="https://github.com/mondbr/pands-project/blob/main/2_histogram_of_sepal_length.png" width=70% height=70%>


<img src="https://github.com/mondbr/pands-project/blob/main/3_histogram_of_sepal_width.png" width=70% height=70%>


<img src="https://github.com/mondbr/pands-project/blob/main/4_histogram_of_petal_length.png" width=70% height=70%>


<img src="https://github.com/mondbr/pands-project/blob/main/5_histogram_of_petal_width.png" width=70% height=70%>



##### *def* *iris_histograms():*


Next function *def iris_histograms():* presents histograms, but with grouping by each species. I used two different approaches of how to plot it: by using *sns.histplot()* and *plt.figure()* with *plt.hist()*. While both ways are presenting same information, the way how they are presented in the plots are slighlt different in the terms of aestetic.  

I was reffering to information found in following sources [geeksforgeeks.org](https://www.geeksforgeeks.org/how-to-make-histograms-with-density-plots-with-seaborn-histplot/) and [geeksforgeeks.org](https://www.geeksforgeeks.org/matplotlib-pyplot-hist-in-python/)

The code with *sns.histplot()*:

    # Creating a separate histogram for 2nd variable Sepal Width for each species using seaborn 
    sns.histplot(data=df, x='sepal_width', hue='species', palette='Set1', edgecolor='none')

    # Add title
    plt.title('Figure 7. Histogram of Sepal Width for Each Species', size = 10)


    # Saving the plot in the repository
    plt.savefig('7_sepal_width_histogram_species.png')

    plt.show()


The code with *plt.figure()* with *plt.hist()*

 Creating a separate histogram for each species for 4rd variable Petal Width
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


Let's see the output also available in this repository 

<img src="https://github.com/mondbr/pands-project/blob/main/6_sepal_length_histogram_species.png" width=70% height=70%>


<img src="https://github.com/mondbr/pands-project/blob/main/7_sepal_width_histogram_species.png" width=70% height=70%>



<img src="https://github.com/mondbr/pands-project/blob/main/8_petal_length_histogram_species.png" width=70% height=70%>



<img src="https://github.com/mondbr/pands-project/blob/main/9_petal_width_histogram_species.png" width=70% height=70%>



#### **Summary**

From the above, we can see that Iris Setosa is much smaller than two other species with their petal size, as we can easily differ it by looking at the above histograms. The sepal length and width seem to vary as well but is more consistent for all species together. 


**Scatterplots**

##### *def* *iris_scatterplots():*

Scatterplots were coded to visualise data of two pairs of the similar variables: Comparison of Sepal width and length and Petal width and length comparison. 
Both of these functions I created under function *def iris_scatterplots():*

The code for scatterplot for Sepal lenght and width: 

    # plotting a scatterplot for sepal and width:
        #setting x-axis variable
        x_var_s = 'sepal_length'

        #setting y-axis variable 
        y_var_s = 'sepal_width' 

        # Create a scatter plot with species showed in different color 
        plt.figure(figsize = (8,6))
        sns.scatterplot(x = x_var_s, y = y_var_s, data = df, marker = 'o', hue = 'species', palette = ['blueviolet','navy','fuchsia']) #marker style to circles #hue to specify variable and set different color to each species

        # Adding labels and titles
        plt.xlabel('Sepal length (cm)', size = 10)
        plt.ylabel('Sepal width (cm)', size = 10)
        plt.title('Figure 10. Sepal length and Sepal width comparison', size = 10)
        plt.legend()
        plt.savefig('10_sepal-length-width_scatt.png')
        plt.show()



<img src="https://github.com/mondbr/pands-project/blob/main/10_sepal-length-width_scatt.png" width=70% height=70%>

<img src="https://github.com/mondbr/pands-project/blob/main/11_petal-length-width_scatt.png" width=70% height=70%>


In the comparison of sepal length and sepal width, we can see that grouping Iris setosa is easier than identifying Iris versicolor and Iris virginica. Iris setosa has wider and shorter sepals, where the other species are more difficult to differ based on these features.

When comparing petal length and petal width, the differences between the three species become much clearer. Iris setosa shows clear profile, by its smallest and narrowest petals in comparistion to the others. Iris virginica shows the largest petals in comparison.



##### *def* *iris_pairplot()*

I created a new function and used pairplot (pairwise plot) to plot pairwise relatioship between multiple variables in a dataset. It plots each numeric variable against each other numeric variable, creating a grid of scatter plots.
The below code creates a pairplot for the numerical variables in the Iris dataset, with different colors for each species. 
It can give a better comparision and observation of the data in a nice-looking way. 
There are four different viariables in this plot, therefore the matrix of scatter plots is 4 x 4 . 

To create a pairplot I used *sns.pairplot()* which is a function from the Seaborn library that creates a pairplot. The parameters such as *vars=numeric_vars* specifies which variables I select to plot, *hue='species'* colors the points for different species, and *palette*, *plot_kws* and *height* are to set the colors and height of my plot. 
I also wanted the layout to be more adjusted, therefore based on information on [stackoverflow.com](https://stackoverflow.com/questions/9603230/how-to-use-matplotlib-tight-layout-with-figure)  and [geeksforgeeks.org](https://www.geeksforgeeks.org/matplotlib-pyplot-subplots_adjust-in-python/) I added a code that allowed me to do it. 



The code is presented as follows:

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

    # Adjusting layout to prevent overlapping parameters
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html
    plt.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.9, hspace=0.4, wspace=0.4)
    plt.show()


<img src="https://github.com/mondbr/pands-project/blob/main/12_pairwise_scatter_plot.png" width=70% height=70%>


**Correlation - linespace and heatmap**

To expand my analysis I decided to use the knowledge from the other module in this semester where I learnt about the correlation and its visualisation in Python. I wanted to check the correlation between two variables and visualise it. To do this, I created two functions: *def iris_linespace():* and def *iris_heatmap():*

##### *def* *iris_linespace():*

From the knowledge from the module *Principles of Data Analytics* I was able to find a **best fit line** (trend line) in my plot. Best fit line defines the optimal relationship of the x-axis and y-axis coordinates of the data points plotted as a scatter plot on the graph. The full guide is available here on [pythonguides.com](https://pythonguides.com/matplotlib-best-fit-line/).

The best fit line or optimal relationship can be achieved by minimizing the distances of the data points from the purposed line.
A linear equation represents a line mathematically. The normal equation of the line is as follows: 


$ y  = mx + c = p_1 x^1 + p_0 = p_1 x + p_0 $

I wanted to use this in this analysis. Therefore I created a new function *def iris_linespace():* so I could create a scatterplot and plot the best fit line to it: 

Here's the code:

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


<img src="https://github.com/mondbr/pands-project/blob/main/13_best_fit_line_petal.png" width=70% height=70%>

The above line on the plot allowes us to predict Petal Width (y) for a given Petal Lenght (x) using the equation of the line $y=mx+c$. In other words if the one variable has higher value, the other one will also be higher, so if the petal is longer, will also be wider. 


##### *def* *iris_heatmap():*

Now let's visualise the correlation between variables. In other words, I wanted to present a correlation matrix as a graphic. To do this, I used *sns.heatmap()* from Seaborn Library. I was reffering to [blog.quantinsti.com](https://blog.quantinsti.com/creating-heatmap-using-python-seaborn/),[datacamp.com](https://www.datacamp.com/tutorial/seaborn-heatmaps) and [geeksforgeeks.org](https://www.geeksforgeeks.org/seaborn-heatmap-a-comprehensive-guide/). 
I created a code that generates a heatmap to visualize the correlation coefficient matrix of the sepal and petal dimensions in the Iris dataset. It shows how strongly each pair of variables is correlated with each other.

The code is: 

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


#### **Summary**
I observed very strong positive correlation (r = 0.96) between Iris petal length and petal width, suggesting that flowers with longer petals are very often wider.

### Finalizing the file 

At the bottom of my analysis.py file I called out all the functions so they can be executed and written to txt file and all plots can be shown to the user. After that I used *sys.stdout = original_stdout* to restore the original standard output. To check if it works, I added a simple code to print the 'END' text in my console to make sure that program has finished. 


## Results:
 
 The summary of the data that was presented in the [summary_analysis.txt](https://github.com/mondbr/pands-project/blob/main/summary_analysis.txt) file allows us to see a varoius of statistical values such as count of each column, average value, standard deviation, minimum values and maximum values etc that gives us a picture of the data that is being reviewed. 
 The sepal lenght of all species vary between 4.3cm and 7.9cm, sepal width vary between 2cm and 4.4cm. 
 Petal parameters are vary from 1cm to 6.9cm for its lenght and 0.1cm to 2.5cm for width.

 Taking into consideration petal length and width, and petal and sepal parameters, Iris virginica has the biggest flowers. Iris Setosa is the smallest in our data. 
 With observed very strong positive correlation (r = 0.96) between Iris petal length and petal width, we can say that flowers with longer petals are very often wider.
 Also strong correlation we can notice between Iris sepal and petal lenght (r = 0.87), so the conclusion can be that both parts of this flower are longer if the Iris grows bigger. 
 
## References:

* Data available at: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv


* Similar analysis and interpretations: 
    * Dan Alexandru on [kaggle.com](https://www.kaggle.com/code/danalexandru/simple-analysis-of-iris-dataset)
    * [Hackers Realm](https://www.hackersrealm.net/post/iris-dataset-analysis-using-python)
    * Ritvik Raj on [rajritvikblog](https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/)
    * Abishek Gupta on [kaggle.com](https://www.kaggle.com/code/abhishekkrg/python-iris-data-visualization-and-explanation)
    * CHAKRA on [kaggle.com](https://www.kaggle.com/code/aschakra/iris-data-visualization-using-python)


* My knowledge mine:
    * Programming and Scripting module by Andrew Beatty on Higher Diploma in Data Analytics course from ATU 2023/24.
    * Principles of Data Analytics module by Ian McLoughlin on Higher Diploma in Data Analytics course from ATU 2023/24.
    * w3schools
    * pandas.pydata.org
    * matplotlib.org
    * geeksforgeeks.org
    * realpython.com
    * chat.openai.com
    * datacamp.com
    * pythonguides.com
    * wikipedia.org
    * numpy.org
    * docs.python.org
    * stackoverflow.com
    * pandas.pydata.org
    * seaborn.pydata.org
    * pythonguides.com
    
    


**Disclaimer:** I used ChatGPT to support me with code refferencing/commenting and enhance the content of this notebook. The notebook is mainly my own work and research, as ChatGPT sometimes suggest clearly incorrect ideas and make mistakes. In any case I had to re-work the code or text it generated to meet my own needs. 


## About me: 

My name is Monika Dabrowska and I am an [ATU](https://www.atu.ie/) student of first semester of the Programming and Scripting module on the Higher Diploma in Data Analytics course during Summer 2023/24.

I am just staring my adventure with programming, so I am using multiple sources and references to help me to complete the assignments. 

If you wish to contact me directly, please email me @ mondbr133@gmail.com

---

### Technologies

* Visual Studio Code version: 1.88.1
* Python version 3.11.5