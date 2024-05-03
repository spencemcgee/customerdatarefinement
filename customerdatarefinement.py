import pandas as pd

def read_text_to_dataframe(txt_filename):
    """
    Read data from a text file and convert it into a DataFrame.

    Args:
        txt_filename (str): The path to the text file.

    Returns:
        pd.DataFrame: The DataFrame containing the data read from the text file.
    """
    df = pd.read_csv(txt_filename, delimiter="|")
    return df

def clean_out_bad_data(df):
    """
    Clean out rows with missing values from the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    df_cleaned = df.dropna()
    return df_cleaned

def combine_columns(group):
    """
    Combine the values of each column into a single string for each group.

    Args:
        group (pd.DataFrame): The DataFrame group to be combined.

    Returns:
        pd.Series: The combined data for the group.
    """
    combined_data = group.iloc[:, :-1].astype(str).apply(lambda x: ', '.join(x), axis=1)
    return combined_data.iloc[0]

def combine_household(df):
    """
    Combine rows with the same address into a single row.

    Args:
        df (pd.DataFrame): The DataFrame to be processed.

    Returns:
        pd.DataFrame: The DataFrame with rows combined by address.
    """
    grouped = df.groupby('address')
    combined_data = pd.DataFrame(columns=df.columns)
    for address, group_df in grouped:
        combined_row = group_df.drop('address', axis=1).apply(lambda x: ', '.join(x.dropna().astype(str)), axis=0)
        combined_row['address'] = address
        combined_data = combined_data._append(combined_row, ignore_index=True)
    return combined_data

# Read data from the text file into a DataFrame
df = read_text_to_dataframe("/content/drive/MyDrive/customerdata/test_data.txt")

# Clean out rows with missing values
df_cleaned = clean_out_bad_data(df)

# Combine rows with the same address into a single row
combined_data = combine_household(df)

# Print the original DataFrame, cleaned DataFrame, and combined DataFrame
print(df)
print(df_cleaned)
print(combined_data)
