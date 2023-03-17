import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from src.components.create_big_table import *
from src.components.create_pie_chart import *
from src.components.select_rows_big_table import *
from src.components.create_chart_datatable import *
from src.components.create_treemap_chart import *
from src.components.updated_tables_chart import *


top_relevant_layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                    ],
                    id="btn-header"
                ),

                html.Div(html.H5("Главная/ Инфографика по наиболее цитируемым статьям")),
                html.Div(html.H2("Инфографика по наиболее цитируемым статьям")),
                html.Div(
                    [
                        'Choose Field',
                        dcc.Dropdown(
                            {'psy': 'Psychology', 'soft': 'Software', 'surg': 'Surgery'},
                            'psy',
                            id='clientside-graph-indicator'
                        )
                    ]
                ),

                html.Div(
                    html.Div(
                        [
                            html.H3("Word count treemap"),
                            dcc.Graph(
                                figure=create_treemap_chart(df_treemap_table),
                                id="treemap-chart",
                                style={'height': 500},
                            )
                        ],
                        id="treemap_container",
                        className="pretty_container",
                    ),
                ),

                html.Div(
                    [
                        html.H3("Top cited table"),
                        dcc.Store(id="selected-rows-big-table"),
                        html.Div(
                            id="big-table",
                        ),
                        html.Div(
                            [
                                html.Button("Download Excel", id="btn-excel-big-table", className="btn-excel"),
                                dcc.Download(id="download-excel-big-table"),
                            ]
                        )
                    ],
                    id="big_table_container",
                    className="pretty_container",
                ),

                html.Div(
                    [
                        html.H3("Document Type"),
                        dcc.Graph(id='circle_doctype')
                    ],
                    id="big_table_container",
                    className="pretty_container",
                ),

                html.Div(
                    [
                        html.H3("Source Title"),
                        dcc.Graph(id='circle_source_title')
                    ],
                    id="big_table_container",
                    className="pretty_container",
                ),

                html.Div(
                    [
                        html.H3("Publisher"),
                        dcc.Graph(id='circle_pub')
                    ],
                    id="big_table_container",
                    className="pretty_container",
                )
            ]
        )
    ]
)


# callbacks


# @app.callback(
#     Output('btn-header', 'children'),
#     Input('url', 'pathname'))
# def create_header_button(pathname):
#     id_btn_home = "button-header.current" if pathname == "/" else "button-header"
#     id_btn_general_info = "button-header.current" if pathname == "/general_info" else "button-header"
#     id_btn_top_cited = "button-header.current" if pathname == "/top_cited" else "button-header"

#     return html.Div(
#         [
#             html.A(html.Button('Начальная страница', id=id_btn_home), href='/'),
#             html.A(html.Button('Общая информация по научной области', id=id_btn_general_info), href='/general_info'),
#             html.A(html.Button('Инфографика по наиболее цитируемым статьям', id=id_btn_top_cited), href='/top_cited')
#         ]
#     )


@app.callback(
    Output("selected-rows-big-table", "data"),
    Input("treemap-chart", "clickData")
)
def selected_rows_table(clickData):
    df = pd.DataFrame(select_rows_big_table(df_big_table_chart, clickData))
    return df.to_json(date_format='iso')


@app.callback(
    Output("big-table", "children"),
    Input("selected-rows-big-table", "data")
)
def update_big_table(data):
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = pd.concat([df_big_table_chart.iloc[data], df_big_table_chart.drop(df_big_table_chart.iloc[data].index)])
    data = [i for i in range(len(data))]
    return create_big_table(dff, data)


@app.callback(
    Output("download-excel-big-table", "data"),
    Input("btn-excel-big-table", "n_clicks"),
    State("selected-rows-big-table", "data"),
    prevent_initial_call=True,
)
def download_big_table(n_clicks, data):
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = df_big_table_chart.iloc[data]
    return dcc.send_data_frame(dff.to_excel, "top_2000_cited_docs.xlsx")


@app.callback(
    Output("circle_doctype", "figure"),
    Input("selected-rows-big-table", "data")
)
def update_pie_chart_doc_type(data):
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = df_big_table_chart.iloc[data]
    return create_pie_chart(dff, 'Document Type')


@app.callback(
    Output("circle_source_title", "figure"),
    Input("selected-rows-big-table", "data")
)
def update_pie_chart_source_title(data):
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = df_big_table_chart.iloc[data]
    return create_pie_chart(dff, 'Source title')


@app.callback(
    Output("circle_pub", "figure"),
    Input("selected-rows-big-table", "data")
)
def update_pie_chart_publisher(data):
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = df_big_table_chart.iloc[data]
    return create_pie_chart(dff, 'Publisher')
