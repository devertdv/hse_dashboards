import pandas as pd
from src.components.read_files import *

authors_dct = {}
sources_dct = {}
countries_dct = {}
fundings_dct = {}
organizations_dct = {}

for _, row in df_big_table.iterrows():

    authors_lst = []
    if not pd.isna(row["Authors"]):
        authors_lst = row["Authors"].split(", ")
    for author in authors_lst:
        authors_dct[author] = authors_dct.get(author, 0) + 1

    sources_lst = []
    if not pd.isna(row["Source title"]):
        source_cell = row["Source title"].replace(u'\xa0', u' ')
        sources_lst = source_cell.split("; ")
    for source in sources_lst:
        source_elem = source.split(", ")[0]
        source_title = source_elem.split("-")[0]
        source_title = source_title.strip()
        sources_dct[source_title] = sources_dct.get(source_title, 0) + 1

    fundings_lst = []
    if not pd.isna(row["Funding Details"]):
        funding_cell = row["Funding Details"].replace(u'\xa0', u' ')
        fundings_lst = funding_cell.split("; ")
    for funding in fundings_lst:
        funding_name = funding.split(", ")[0]
        fundings_dct[funding_name] = fundings_dct.get(funding_name, 0) + 1

    countries_lst = []
    if not pd.isna(row["Affiliations"]):
        countries_lst = row["Affiliations"].split("; ")
    unique_countries = []
    for country in countries_lst:
        country_name = country.split(", ")[-1]
        unique_countries.append(country_name)
    unique_countries = list(set(unique_countries))
    for country in unique_countries:    
        countries_dct[country] = countries_dct.get(country, 0) + 1

    organizations_lst = []
    if not pd.isna(row["Affiliations"]):
        organizations_lst = row["Affiliations"].split("; ")
    for organization in organizations_lst:
        org_property = organization.split(", ")
        for property in org_property:
            if "nivers" in property.lower() or "insti" in property.lower():
                organizations_dct[property] = organizations_dct.get(property, 0) + 1
                break


authors_num_of_docs = []
for _, row in df_authors.iterrows():
    author = " ".join(row["Author"].split(", "))
    authors_num_of_docs.append(authors_dct.get(author, 0))
df_authors["Number of docs"] = authors_num_of_docs


sources_num_of_docs = []
for _, row in df_sources.iterrows():
    sources_num_of_docs.append(sources_dct.get(row["Source"], 0))
df_sources["Number of docs"] = sources_num_of_docs


countries_num_of_docs = []
for _, row in df_countries.iterrows():
    countries_num_of_docs.append(countries_dct.get(row["Country"], 0))
df_countries["Number of docs"] = countries_num_of_docs


fundings_num_of_docs = []
for _, row in df_fundings.iterrows():
    fundings_num_of_docs.append(fundings_dct.get(row["Funding"], 0))
df_fundings["Number of docs"] = fundings_num_of_docs


organizations_num_of_docs = []
for _, row in df_organizations.iterrows():
    organizations_num_of_docs.append(organizations_dct.get(row["Organization"], 0))
df_organizations["Number of docs"] = organizations_num_of_docs
