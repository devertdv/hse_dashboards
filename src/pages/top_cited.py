import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output, State

from app import app
from src.components.create_big_table import *
from src.components.create_pie_chart import *
from src.components.create_chart_datatable import *
from src.components.create_left_column import *
from src.components.create_right_column import *
from src.components.create_treemap_chart import *
from src.components.get_fields import *
from src.components.read_files_big_table import *
from src.components.select_rows_big_table import *


top_relevant_layout = html.Div(
    [
        create_left_column(),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                            ],
                            id="btn-header"
                        ),
                    ]
                ),

                html.Div(
                    [
                        html.Div(html.H2("Инфографика по наиболее цитируемым статьям")),
                        html.Div(
                            [
                                html.P('Выберите научную область'),
                                dcc.Dropdown(
                                    get_fields(),
                                    'Accounting',
                                    id='dropdown-fields'
                                )
                            ],
                        ),

                        html.Div(
                            [
                                dcc.Store(id="treemap-table"),
                                html.H3("Карта ключевых слов"),
                                dcc.Graph(
                                    id="treemap-chart",
                                    style={
                                        'height': 500,
                                    },
                                )
                            ],
                            id="treemap_container",
                            className="pretty_container",
                        ),

                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H3("Таблица наиболее цитируемых источников"),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Button("Скачать краткую версию", id="btn-excel-big-table", className="btn-excel"),
                                                        dcc.Download(id="download-excel-big-table"),
                                                    ]
                                                ),
                                                html.Div(
                                                    [
                                                        html.Button("Скачать полную версию", id="btn-excel-full-big-table", className="btn-excel"),
                                                        dcc.Download(id="download-excel-full-big-table"),
                                                    ]
                                                ),
                                            ],
                                            className="flex-display"
                                        )
                                    ],
                                    className="row-chart-datatable"
                                ),
                                dcc.Store(id="selected-rows-big-table"),
                                dcc.Store(id="full-big-table-df"),
                                dcc.Store(id="short-big-table-df"),
                                html.Div(
                                    id="big-table",
                                ),
                            ],
                            id="big_table_container",
                            className="pretty_container",
                        ),

                        html.Div(
                            [
                                html.H3("Распределение по типам публикации"),
                                dcc.Graph(id='circle_doctype')
                            ],
                            id="big_table_container",
                            className="pretty_container",
                        ),

                        html.Div(
                            [
                                html.H3("Распределение по журналам"),
                                dcc.Graph(id='circle_source_title')
                            ],
                            id="big_table_container",
                            className="pretty_container",
                        ),

                        html.Div(
                            [
                                html.H3("Распределение по публикующим ресурсам"),
                                dcc.Graph(id='circle_pub')
                            ],
                            id="big_table_container",
                            className="pretty_container",
                        )
                    ]
                )
            ],
            style={
                "margin-left": "12%",
                "margin-right": "12%",
            }
        ),
        create_right_column(),
    ]
)


# callback read_files


@app.callback(
    Output('full-big-table-df', 'data'),
    Input('dropdown-fields', 'value'))
def upload_files_authors(value):
    df = read_files_big_table(value)
    return df.to_json(date_format='iso')


@app.callback(
    Output('short-big-table-df', 'data'),
    Input('dropdown-fields', 'value'))
def upload_files_authors(value):
    df = read_files_big_table(value)
    df = df.iloc[:, [0, 2, 3, 4, 17, 38, 49, 13]]
    return df.to_json(date_format='iso')


# callback big_table


@app.callback(
    Output("selected-rows-big-table", "data"),
    Input("treemap-chart", "clickData"),
    Input("short-big-table-df", "data")
)
def selected_rows_table(clickData, data):
    dff = pd.read_json(data)
    df = pd.DataFrame(select_rows_big_table(dff, clickData))
    return df.to_json(date_format='iso')


@app.callback(
    Output("big-table", "children"),
    Input("selected-rows-big-table", "data"),
    Input("short-big-table-df", "data")
)
def update_big_table(data, data_df):
    df_big_table = pd.read_json(data_df)
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = pd.concat([df_big_table.iloc[data], df_big_table.drop(df_big_table.iloc[data].index)])
    data = [i for i in range(len(data))]
    return create_big_table(dff, data)


@app.callback(
    Output("download-excel-big-table", "data"),
    Input("btn-excel-big-table", "n_clicks"),
    State("short-big-table-df", "data"),
    State("selected-rows-big-table", "data"),
    prevent_initial_call=True,
)
def download_big_table(n_clicks, data_df, data):
    df_big_table = pd.read_json(data_df)
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = df_big_table.iloc[data]
    return dcc.send_data_frame(dff.to_excel, "top_2000_cited_docs.xlsx")


@app.callback(
    Output("download-excel-full-big-table", "data"),
    Input("btn-excel-full-big-table", "n_clicks"),
    State("full-big-table-df", "data"),
    prevent_initial_call=True,
)
def download_big_table(n_clicks, data_df):
    df_big_table = pd.read_json(data_df)
    return dcc.send_data_frame(df_big_table.to_excel, "full_top_2000_cited_docs.xlsx")


# callbacks charts


@app.callback(
    Output("treemap-chart", "figure"),
    Input("short-big-table-df", "data")
)
def update_treemap_chart(data):
    df = pd.read_json(data)
    df_treemap_table = df.loc[:, ["Author Keywords"]]
    df_treemap_table = df_treemap_table.rename(columns={"Author Keywords": "keywords"})
    df_treemap_table = df_treemap_table[~df_treemap_table["keywords"].isnull()]
    return create_treemap_chart(df_treemap_table)


@app.callback(
    Output("circle_doctype", "figure"),
    Input("selected-rows-big-table", "data"),
    Input("short-big-table-df", "data")
)
def update_pie_chart_doc_type(data, data_df):
    df_big_table = pd.read_json(data_df)
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = df_big_table.iloc[data]
    return create_pie_chart(dff, 'Document Type')


@app.callback(
    Output("circle_source_title", "figure"),
    Input("selected-rows-big-table", "data"),
    Input("short-big-table-df", "data")
)
def update_pie_chart_source_title(data, data_df):
    df_big_table = pd.read_json(data_df)
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = df_big_table.iloc[data]
    return create_pie_chart(dff, 'Source title')


@app.callback(
    Output("circle_pub", "figure"),
    Input("selected-rows-big-table", "data"),
    Input("short-big-table-df", "data")
)
def update_pie_chart_publisher(data, data_df):
    df_big_table = pd.read_json(data_df)
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = df_big_table.iloc[data]
    return create_pie_chart(dff, 'Publisher')
