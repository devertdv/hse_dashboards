import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from src.components.bar_chart import *
from src.components.big_table import *
from src.components.pie_chart import *
from src.components.select_rows_big_table import *
from src.components.table_chart import *
from src.components.treemap_chart import *
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
                html.Div(
                    [
                        'Field',
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
                        dcc.Store(id="selected-rows-big-table"),
                        html.Div(
                            id="big-table",
                        ),
                        html.Div(
                            [
                                html.Button("Download CSV", id="btn-csv-big-table", className="btn-csv"),
                                dcc.Download(id="download-csv-big-table"),
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
    Output("circle_doctype", "figure"),
    Input("treemap-chart", "clickData")
)
def update_pie_chart(clickData):
    return create_pie_chart(df_big_table_chart,'Document Type', clickData)


@app.callback(
    Output("circle_source_title", "figure"),
    Input("treemap-chart", "clickData")
)
def update_pie_chart(clickData):
    return create_pie_chart(df_big_table_chart,'Source title', clickData)


@app.callback(
    Output("circle_pub", "figure"),
    Input("treemap-chart", "clickData")
)
def update_pie_chart(clickData):
    return create_pie_chart(df_big_table_chart,'Publisher', clickData)


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
    return create_big_table(df_big_table_chart, data)


@app.callback(
    Output("download-csv-big-table", "data"),
    Input("btn-csv-big-table", "n_clicks"),
    State("selected-rows-big-table", "data"),
    prevent_initial_call=True,
)
def func(n_clicks, data):
    df = pd.read_json(data)
    data = df[0].tolist()
    dff = df_big_table_chart.iloc[data]
    return dcc.send_data_frame(dff.to_csv, "top_2000_docs_by_relevance.csv")
