import numpy as np 
import pandas as pd

def prob4():
    '''
    Purpose:
        The purpose of this function is to show how to visulize the fundemantals of the dataframe like the head and tail, info and describe. 
        Also how to find null and NAN number values and then to drop them.

    Parameters: 
        There are no parameters being passed as arguments here. 

    Return: 
        Datafame manipulations are printed and a final return of the dataframe is done also for testing to see if the sum of nulls is zero and the row count is 
        under 150 showing that the drop actually happened.  
    '''
    data = pd.read_csv('/Users/natcabrera101/Desktop/IrisData.csv')

    print(data.head(10))
    print()
    print(data.tail(10))
    print()
    
    print(data.info())
    print()
    print(data.describe())
    
    df = pd.DataFrame(data)
    
    null_mask = df.isnull() #Shows true and false, True for NAN values. 
    print(null_mask)
    
    null_mask_filter = df.isnull().any(axis=1) #Mask to show all rows where theres at least one null value, True = missing
    print(null_mask_filter)
    
    df = df.dropna(axis=0, how='any')
    print(df)
    
    row_count = len(df)
    print(row_count)
    
    return df

if __name__ == "__main__":
    
    df = prob4()
    assert df.isna().sum().sum() == 0
    assert len(df) < 150