import pandas as pd

df_authors = pd.read_csv('data/authors_rate.csv', header=None, sep=",")
df_authors.columns = ["Author", "Rate"]
df_authors = df_authors[df_authors.Author != "Undefined"]
df_authors.sort_values("Rate", ascending=True)

df_organizations = pd.read_csv('data/organizations_rate.csv', header=None, sep=",")
df_organizations.columns = ["Organization", "Rate"]
df_organizations = df_organizations[df_organizations.Organization != "Undefined"]
df_organizations.sort_values("Rate", ascending=True)

df_fundings = pd.read_csv('data/funding_rate.csv', header=None, sep=",")
df_fundings.columns = ["Funding", "Rate"]
df_fundings = df_fundings[df_fundings.Funding != "Undefined"]
df_fundings.sort_values("Rate", ascending=True)

df_countries = pd.read_csv('data/countries_rate.csv', header=None, sep=",")
df_countries.columns = ["Country", "Rate"]
df_countries = df_countries[df_countries.Country != "Undefined"]
df_countries.sort_values("Rate", ascending=True)

df_sources = pd.read_csv('data/sources_rate.csv', header=None, sep=",")
df_sources.columns = ["Source", "Rate"]
df_sources = df_sources[df_sources.Source != "Undefined"]
df_sources.sort_values("Rate", ascending=True)

df_dynamics = pd.read_csv('data/publications_dinamic.csv', header=None, sep=",")
df_dynamics.columns = ["Year", "Number"]

df_big_table = pd.read_csv('data/top-2000_pub_by citation.csv', sep=',')
df_big_table["Author Keywords"] = df_big_table["Author Keywords"].fillna('')
df_big_table["Author Keywords"] = df_big_table["Author Keywords"].apply(str.lower)
df_big_table["Year"] = df_big_table["Year"].astype('object')
df_big_table_chart = df_big_table.iloc[:, [0, 2, 3, 4, 17, 38, 49, 13]]

df_treemap_table = df_big_table.loc[:, ["Author Keywords"]]
df_treemap_table = df_treemap_table.rename(columns={"Author Keywords": "keywords"})
df_treemap_table = df_treemap_table[~df_treemap_table["keywords"].isnull()]
