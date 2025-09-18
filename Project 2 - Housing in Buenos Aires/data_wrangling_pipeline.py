import pandas as pd


def wrangle(filepath):
    """Helps to preprocess operations for dataframe"""
    # Read CSV file into DataFrame
    df = pd.read_csv(filepath, index_col=0)
    
    #Subset to properties in "Capital Federal"
    df = df[df["place_with_parent_names"].str.contains("Capital Federal")]

    #Subet to apartments
    df = df[df["property_type"]=="apartment"]   
    
    #Subset to properties where "price approx usd" is less than 400000
    df = df[df["price_aprox_usd"]<400_000] 
    
    #Remove outliers by "surface_covered_in_m2"
    low,high=df["surface_covered_in_m2"].quantile([0.1,0.9])
    df=df[df["surface_covered_in_m2"].between(low,high)]
    df[["lat","lon"]]=df["lat-lon"].str.split(",", expand=True).astype(float)
    df.drop(columns=["lat-lon"], inplace=True)


    # Get place name
    df["neighborhood"] = df["place_with_parent_names"].str.split("|", expand=True)[3]
    df.drop(columns="place_with_parent_names", inplace=True)

    
    # Drop features with high null counts
    df.drop(columns=["floor", "expenses"], inplace=True)
    # Drop low and high cardinality categorical variables
    df.drop(columns=["operation","property_type","properati_url","currency"], inplace=True)

    #Drop data leakage features
    df.drop(columns=[
        "price",
        "price_aprox_local_currency",
        "price_per_m2",
        "price_usd_per_m2"
        ] , inplace=True)

    #Drop correlated features (columns with multicollinearity)
    df.drop(columns=[
        "surface_total_in_m2",
        "rooms"
    ], inplace=True)

    return df


def input_for_matplotlib(ax):

    ax.set_xlabel(input("Enter label for x: "))
    ax.set_ylabel(input("Enter label for y: "))
    ax.set_title(input("Enter Title: "))
    return ax