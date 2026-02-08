
import numpy as np
import pandas as pd

def prob2():
    '''
    Purpose:
        This function is designed to show how to form a data frame with multiple rows and columns. 
        It also shows how to manipulate the index with set_index() and print/locating certain
        parts of the dataframe like using iloc and loc. 

    Parameters: 
        There are no parameters being passed as arguments here but dataframe is the main variable being 
        acted on. 

    Return: 
        There are no returns here but there are dataframes being printed and selections as well
        being printed. 

    '''
    
    df = pd.DataFrame({
        "2018":[85, 73, 80, 64], 
        "2019":[60, 80, 58, 96], 
        "2020":[90, 64, 74, 87], 
        "2021":[85, 83, 79, 82], 
        "2022":[92, 93, 100, 83], 
        "Subjects":['Math', 'Science', 'English', 'Arts']
        
    })
    
    print(df)
    
    df = df.set_index("Subjects")
    print(df)
    print()
    
    print(df.loc[['Math', 'English']])
    print()
    
    print(df.loc["Math":"English", "2019":"2021"])
    print()
    
    print(df.iloc[[0,2]])
    print()
    
    print(df.iloc[0:3, 1:4])
    print()
    
    return df
    
if __name__ == "__main__": 
    
    df = prob2()
    
    assert df.index.name == "Subjects"
    assert df.loc["Math", "2019"] == 60
