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

# Aggregate a target value inside a dataframe column by its mean values.
# tagret_val = Column of values we want aggregated(This is string)
# int_worth = Column of the corresponding worth(i.e price)(This column head is also a string)
# the mean worth 
def aggreate_col_val(dataframe,column_val: str,column_worth: str):
    # Returns a series of the top 5 brands, we can acces the specific brand of this series by
    # referencing its index label.
    total_val= dataframe[target_val].value_counts()
    avg_price = 0
    brand_mean_dict = {}   
    # Take advantage a vectorization in pandas to compute mean of our target column
    for brand in total_val.index:
         avg_price = autos.loc[autos[target_val]==brand,int_worth].mean()#
         brand_mean_dict[brand]= int(avg_price)
    return brand_mean_dict


