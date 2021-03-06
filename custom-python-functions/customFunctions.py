import pandas as pd

# Iterate through string, append "_" to character
# strip "_" if it was appended directly at the beginning or end of a word
# return the snakecase string
def change_to_camelcase(string):
    new_string = ""
    for char in string:
        if char.isupper():
            char = char.lower()
            new_string += "_"+char
        else:
            new_string += char
    new_string = new_string.strip("_")
    return new_string

# Aggregate a target value inside a dataframe column to a mean value.
# tagret_val = Column of values we want aggregated(This is string)
# int_worth = Column of the corresponding value worth(i.e price)(This column head is also a string)
# dataframe = DataFrame object created using the pandas library
def aggreate_col_val(dataframe,column_val: str,column_worth: str):

    total_val= dataframe[column_val].value_counts()
    avg_price = 0
    mean_dict = {}   
    # Take advantage a vectorization in pandas to compute mean of our target column
    for value in total_val.index:
         avg_price = dataframe.loc[autos[column_val]==value,column_worth].mean()
         mean_dict[value]= int(avg_price)
    return mean_dict


