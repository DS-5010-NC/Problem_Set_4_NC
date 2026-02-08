import pandas as pd
import numpy as np 

def prob1(): 
    '''
    Purpose: 
        This is designed to show how to use multiple data sources and join them into one
        data frame. For example using a list, array, and dictionary and then forming a data frame.

    Parameters: There are no arguments passed here, but multiple variables within the function. 

    Return: This returns the resulting dataframe. 

    '''
    
    string_list = ["String1", "String2", "String3", "String4", "String5"]
    string_series = pd.Series(string_list).reset_index(drop=True)
    print(string_series)
    print() #I am only inlcuding print statements visually for spaces in terminal output, not apart of the 3 lines of code for the problem 
    
    arr = np.random.randint(1, 101,(5))
    arr_series = pd.Series(arr).reset_index(drop=True)
    print(arr_series)
    print()
    
    data_dict = {"String1": 10,"String2": 25, "String3": 15, "String4": 30, "String5": 20}
    dict_series = pd.Series(data_dict).reset_index(drop=True)
    print(dict_series)
    
    
    df = pd.DataFrame({
        "StringData": string_series, 
        "RandomIntegers": arr_series,
        "DictionaryData":dict_series
    })

    print(df)
    return df
    

if __name__ == "__main__":
    
    df = prob1()
    assert df.shape == (5,3)
    assert df["StringData"].iloc[0] == "String1"