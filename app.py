import pandas as pd

import dash
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from src.components.read_files import *
from src.components.bar_chart import *
from src.components.datatable import *

# Инициализируем сервер
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            [
                html.Div(
                    [
                        html.H3("Authors rate table"),
                        create_datatable(df_authors),
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),
                html.Div(
                    id='figure-author',
                    className="pretty_container four columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H3("Organizations rate table"),
                        create_datatable(df_organizations),
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),
                html.Div(
                    id='figure-organization',
                    className="pretty_container four columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H3("Fundings rate table"),
                        create_datatable(df_fundings),
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),
                html.Div(
                    id='figure-funding',
                    className="pretty_container four columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H3("Countries rate table"),
                        create_datatable(df_countries),
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),
                html.Div(
                    id='figure-country',
                    className="pretty_container four columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H3("Sources rate table"),
                        create_datatable(df_sources),
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),
                html.Div(
                    id='figure-source',
                    className="pretty_container four columns",
                ),
            ],
            className="row flex-display",
        )
    ]
)


@app.callback(
    Output('figure-author', "children"),
    Input('table-with-figure-author', "selected_rows"))
def update_figure_authors(selected_rows):
    return html.Div(
            [
                html.H3("Authors rate bar chart"),
                dcc.Graph(
                    figure=create_bar_chart(df_authors, selected_rows),
                    style={
                        'overflowY': 'scroll',
                        'height': 300,
                        'width': 620
                    }
                ),
            ]
    )

@app.callback(
    Output('figure-organization', "children"),
    Input('table-with-figure-organization', "selected_rows"))
def update_figure_organizations(selected_rows):
    return html.Div(
            [
                html.H3("Organizations rate bar chart"),
                dcc.Graph(
                    figure=create_bar_chart(df_organizations, selected_rows),
                    style={
                        'overflowY': 'scroll',
                        'height': 300,
                        'width': 620
                    }
                ),
            ]
    )

@app.callback(
    Output('figure-funding', "children"),
    Input('table-with-figure-funding', "selected_rows"))
def update_figure_fundings(selected_rows):
    return html.Div(
            [
                html.H3("Fundings rate bar chart"),
                dcc.Graph(
                    figure=create_bar_chart(df_fundings, selected_rows),
                    style={
                        'overflowY': 'scroll',
                        'height': 300,
                        'width': 620
                    }
                ),
            ]
    )

@app.callback(
Output('figure-country', "children"),
Input('table-with-figure-country', "selected_rows"))
def update_figure_countries(selected_rows):
    return html.Div(
            [
                html.H3("Countries rate bar chart"),
                dcc.Graph(
                    figure=create_bar_chart(df_countries, selected_rows),
                    style={
                        'overflowY': 'scroll',
                        'height': 300,
                        'width': 620
                    }
                ),
            ]
    )


@app.callback(
Output('figure-source', "children"),
Input('table-with-figure-source', "selected_rows"))
def update_figure_sources(selected_rows):
    return html.Div(
            [
                html.H3("Sources rate bar chart"),
                dcc.Graph(
                    figure=create_bar_chart(df_sources, selected_rows),
                    style={
                        'overflowY': 'scroll',
                        'height': 300,
                        'width': 620
                    }
                ),
            ]
    )


if __name__ == '__main__':
    app.run_server(debug=True)
