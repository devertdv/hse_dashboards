from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from src.components.bar_chart import *
from src.components.big_table import *
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
                        dbc.NavLink("Инфографика по наиболее релевантным статьям", href="/top_relevant", active="exact"),
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
                        html.Div(
                            id="big-table",
                        ),
                    ]
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
    Output("big-table", "children"),
    Input("treemap-chart", "clickData")
)
def update_big_table(clickData):
    return create_big_table(df_big_table, clickData)
