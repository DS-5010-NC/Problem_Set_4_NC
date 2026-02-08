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

def prob5(df):
    '''
    Purpose:
        The purpose of this function is to show how to visulize counts in a dataframe and then manipulate them. 
        Aso how to use methods like idx_max, filters and correlation features 

    Parameters: 
        The dataframe from prob 4 is being passed to use in prob 5 here

    Return: 
        Datafame manipulations are printed and a final return of the dataframe  counts and final_corr is done also for testing puproses. 
    '''
    print()
    print("Problem 5:")
    print()
    
    counts = df["species"].value_counts()
    print(f"DataFrame counts: {counts}")
    print()
    
    s = df.duplicated()
    print()
    print(s)
    print(df[s])
    
    filtered = df[(df["sepal_length"] > 5) & (df["sepal_width"] > 3)]
    print(f"filtered: {filtered}")
    print()
    
    idx_max = df.idxmax()
    print(f"idxmax:\n[{idx_max}]")
    print()
    
    corr_vals = df[["sepal_length", "sepal_width",  "petal_length",  "petal_width"]].corr()
    sepal_corr = corr_vals["sepal_length"].drop("sepal_length")
    final_corr = sepal_corr.abs().idxmax()
    print(f"Correlations: {final_corr}")
    
    return counts, final_corr
    
if __name__ == "__main__":
    
    df = prob4()
    counts, final_corr = prob5(df) 
    
    assert df.isna().sum().sum() == 0
    assert counts.idxmax() == "virginica"
    assert final_corr == "petal_length"



