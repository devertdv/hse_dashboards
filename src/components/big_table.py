import pandas as pd
from dash import dash_table

def create_big_table(df, click_data):
    
    select_rows = ''
    if click_data is not None and "entry" in click_data["points"][0] and click_data["points"][0]["entry"] != click_data["points"][0]["label"]:
        keyword = click_data["points"][0]["label"]
        select_rows = df.index[df["Author Keywords"].str.contains(keyword, regex=False)].tolist()
    else:
        select_rows = [i for i in range(df.shape[0])]

    return dash_table.DataTable(
                        data=df.iloc[:, [0, 2, 3, 4, 13, 17, 38, 49]].to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in df.iloc[:, [0, 2, 3, 4, 13, 17, 38, 49]].columns],

                        fixed_rows={'headers': True},
                        sort_action="native",
                        sort_mode="single",
                        sort_by=[],
                        editable=True,
                        filter_action="native",
                        row_selectable='multi',
                        selected_rows=select_rows,
                        page_action='native',
                        page_current= 0,
                        page_size= 10,

                        style_table={
                            'height': 500,
                        },
                        style_cell={
                            'minWidth': 200,
                            'width': 200,
                            'maxWidth': 200,
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                        },
                        style_data={
                            'whiteSpace': 'normal',
                            'height': 'auto',
                        },
                    )