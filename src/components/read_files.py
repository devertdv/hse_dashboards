import pandas as pd

df_authors = pd.read_csv('data/authors_rate.csv', header=None, sep=",")
df_authors.columns = ["Author", "Rate"]
df_authors.sort_values("Rate", ascending=True)

df_organizations = pd.read_csv('data/organizations_rate.csv', header=None, sep=",")
df_organizations.columns = ["Organization", "Rate"]
df_organizations.sort_values("Rate", ascending=True)

df_fundings = pd.read_csv('data/funding_rate.csv', header=None, sep=",")
df_fundings.columns = ["Funding", "Rate"]
df_fundings.sort_values("Rate", ascending=True)

df_countries = pd.read_csv('data/countries_rate.csv', header=None, sep=",")
df_countries.columns = ["Country", "Rate"]
df_countries.sort_values("Rate", ascending=True)

df_sources = pd.read_csv('data/sources_rate.csv', header=None, sep=",")
df_sources.columns = ["Source", "Rate"]
df_sources.sort_values("Rate", ascending=True)