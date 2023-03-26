import pandas as pd


def read_files_big_table(field):
    df_big_table = pd.read_csv(f'data/{field}/top-2000_pub_by citation.csv', sep=',')
    df_big_table["Author Keywords"] = df_big_table["Author Keywords"].fillna('')
    df_big_table["Author Keywords"] = df_big_table["Author Keywords"].apply(str.lower)
    df_big_table["Year"] = df_big_table["Year"].astype('object')
    return df_big_table
