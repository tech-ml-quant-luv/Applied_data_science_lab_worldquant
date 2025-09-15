import pandas as pd


def wrangle(filepath):
    # Read CSV file into DataFrame
    df = pd.read_csv(filepath)
    
    #Subset to properties in "Capital Federal"
    df = df[df["place_with_parent_names"].str.contains("Capital Federal")]

    #Subet to apartments
    df = df[df["property_type"]=="apartment"]   
    
    #Subset to properties where "price approx usd" is less than 400000
    df = df[df["price_aprox_usd"]<400_000] 
    
    #Remove outliers by "surface_covered_in_m2"
    low,high=df["surface_covered_in_m2"].quantile([0.1,0.9])
    df=df[df["surface_covered_in_m2"].between(low,high)]

    return df

