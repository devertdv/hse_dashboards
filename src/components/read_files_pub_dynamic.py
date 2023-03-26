import pandas as pd


def read_files_pub_dynamic(field):
    try:
        df = pd.read_csv(f'data/{field}/publications_dinamic.csv', on_bad_lines='skip', header=None)
        if df.shape[1] > 2:
            df = df.iloc[:, 1:]
        elif df.shape[1] < 2:
            raise pd.errors.ParserError
    except pd.errors.ParserError:
        df = pd.read_csv(f'data/{field}/publications_dinamic.csv', skiprows=7, on_bad_lines='skip', header=None)
    if df.shape[1] != 2:
        df = df.iloc[:, 1:]
    df.columns = ["Year", "Number"]
    return df
