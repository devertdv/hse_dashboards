import pandas as pd


def read_files_sources(field):
    try:
        df = pd.read_csv(f'data/{field}/sources_rate.csv', on_bad_lines='skip', header=None)
        if df.shape[1] > 2:
            df = df.iloc[1:, 1:]
        elif df.shape[1] < 2:
            raise pd.errors.ParserError
    except pd.errors.ParserError:
        df = pd.read_csv(f'data/{field}/sources_rate.csv', skiprows=8, on_bad_lines='skip', header=None)
    df.columns = ["Source", "Rate"]
    df = df[df.Source != "Undefined"]
    df.sort_values("Rate", ascending=True)
    return df
