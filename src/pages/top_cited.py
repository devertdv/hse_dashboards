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
                html.H2("Навигация", className="display-4"),
                html.Hr(),
                html.P(
                    "Выберите интересующий раздел", className="lead"
                ),
                dbc.Nav(
                    [
                        dbc.NavLink("Начальная страница", href="/", active="exact"),
                        html.Hr(),
                        dbc.NavLink("Общая информация по научной области", href="/general_info", active="exact"),
                        html.Hr(),
                        dbc.NavLink("Инфографика по наиболее цитируемым статьям", href="/top_cited", active="exact"),
                    ],
                    vertical=True,
                    pills=True,
                ),
            ],
            style={
                "position": "fixed",
                "top": 0,
                "left": 0,
                "bottom": 0,
                "width": "15%",
                "padding": "2rem 1rem",
                "background-color": "#f8f9fa",
            },
        ),

        html.Div(
            [
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
            ],
            style={
                "margin-left": "17%",
                "margin-right": "2rem",
                "padding": "2rem 1rem",
            }
        )
    ]
)


# callbacks


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
