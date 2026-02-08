import numpy as np 
import pandas as pd
import statistics as statistics 

def prob3(): 
    '''
    Purpose:
        The purpose of this function is to show how to manipulate a dataframe.
    
    Parameters: 
        There are no parameters being passed as arguments here. 
    
    Return: 
        Datafame manipulations are printed and a final retrun of the dataframe is done also for testing. 
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
    
    df.loc[:, "2019"] =df.loc[:, "2019"] + 3
    print(df)
    
    df.loc["Math","2021"] = 95
    print(df)
    
    df["Mean"] = df[["2018", "2019", "2020", "2021", "2022"]].mean(axis=1)
    df = df.sort_index()
    print(df)
    
    print(df["2020"].min())
    print()
    
    df = df.drop(["Science", "Arts"])
    print(df)
    
    df =df.drop(columns=["2021"])
    print(df)
    
    return df

if __name__ == "__main__":
    
    df = prob3()
    assert "Mean" in df.columns





    