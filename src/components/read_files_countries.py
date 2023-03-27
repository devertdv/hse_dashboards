import pandas as pd


def read_files_countries(field):
    try:
        df = pd.read_csv(f'data/{field}/countries_rate.csv', on_bad_lines='skip', header=None)
        if df.shape[1] > 2:
            df = df.iloc[1:, 1:]
        elif df.shape[1] < 2:
            raise pd.errors.ParserError
    except pd.errors.ParserError:
        df = pd.read_csv(f'data/{field}/countries_rate.csv', skiprows=8, on_bad_lines='skip', header=None)
    df.columns = ["Country", "Rate"]
    df = df[df.Country != "Undefined"]
    df.sort_values("Rate", ascending=True)
    return df

