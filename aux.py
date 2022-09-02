import pandas as pd
import numpy as np

# Define a function to find outliers and NaN values in a dataset, and replace it by the column mean.
def find_outliers(my_data):
    # definition of numeric types
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

    # Take numeric columns
    data = my_data.select_dtypes(include=numerics)

    # Take column names
    columns = data.columns
    
    # Set the new dataframe
    out = pd.DataFrame()

    # Number of outliers
    n_outliers = 0

    for column in columns:
        """
        For each column, calculate the lower and the upper fences.
        Iterate each value in the column:
            if the value is between the fences: add to the new column
            it not: dropt it, replace with the column mean and add to the new column
        After iteration, add column to the new dataframe. After  iterate all columns,
        add excluded columns to the dataframe and return it and the number of outliers.
        """
        Q1 = data[column].describe().describe()['25%']
        Q3 = data[column].describe().describe()['75%']
        IQR = Q3-Q1

        lower_fence = Q1 - 1.5*IQR
        upper_fence = Q3 + 1.5*IQR
        
        new_column = pd.Series(dtype='float64')
        for idx, value in enumerate(data[column]):
            """ This conditional statement allows us to replace either outliers or NaN values.
            """
            if ((value >= lower_fence) & (value <= upper_fence)):
                new_value = pd.Series(data=value, index=[idx])
                new_column = pd.concat([new_column, new_value])
            else:
                col_mean  = np.mean(data[column].drop(idx))
                new_value = pd.Series(data=col_mean, index=[idx])
                new_column = pd.concat([new_column, new_value])
                n_outliers = n_outliers + 1
        new_column.name = column
        new_column = pd.DataFrame(new_column)
        out = pd.concat([out, new_column], axis=1)

    excluded_columns = my_data.select_dtypes(exclude=numerics)
    out = pd.concat([out, excluded_columns], axis=1)

    return (out, n_outliers)

# Define a function to apply find_outliers() iteratively
def replace_outliers(my_data):
    """
    While the number of outliers is not equal to 0, the loop will apply the
    function find_outliers(). 
    """
    data = my_data
    n_outliers = -1
    n_loops = 0
    total_outliers = 0

    while(n_outliers != 0):
        data, n_outliers = find_outliers(data)
        n_loops = n_loops+1
        total_outliers = total_outliers + n_outliers
        
    print('***Found a total of '+str(total_outliers)+' outliers over '+str(n_loops)+' iterations.***\n')
    
    return data