from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
from src.components.create_bar_chart_docs_num import *
from src.components.create_bar_chart_rate import *
from src.components.create_chart_datatable import *
from src.components.updated_tables_chart import *


general_info_layout = html.Div(
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
                html.Div(html.H5("Главная/ Общая информация по научной области")),
                html.Div(html.H2("Общая информация по научной области")),
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
                    [
                        html.Div(
                            [
                                html.H3("Authors rate table"),
                                create_chart_datatable(df_authors),
                                html.Div(
                                    [
                                        html.Button("Download Excel", id="btn-excel-author", className="btn-excel"),
                                        dcc.Download(id="download-excel-author"),
                                    ]
                                )
                            ],
                            id="cross-filter-options",
                            className="pretty_container",
                        ),
                        html.Div(
                            id='figure-author',
                            className="pretty_container",
                        ),
                    ],
                    className="row flex-display",
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                html.H3("Organizations rate table"),
                                create_chart_datatable(df_organizations),
                                html.Div(
                                    [
                                        html.Button("Download Excel", id="btn-excel-organization", className="btn-excel"),
                                        dcc.Download(id="download-excel-organization"),
                                    ]
                                )
                            ],
                            id="cross-filter-options",
                            className="pretty_container",
                        ),
                        html.Div(
                            id='figure-organization',
                            className="pretty_container",
                        ),
                    ],
                    className="row flex-display",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3("Fundings rate table"),
                                create_chart_datatable(df_fundings),
                                html.Div(
                                    [
                                        html.Button("Download Excel", id="btn-excel-funding", className="btn-excel"),
                                        dcc.Download(id="download-excel-funding"),
                                    ]
                                )
                            ],
                            id="cross-filter-options",
                            className="pretty_container",
                        ),
                        html.Div(
                            id='figure-funding',
                            className="pretty_container",
                        ),
                    ],
                    className="row flex-display",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3("Countries rate table"),
                                create_chart_datatable(df_countries),
                                html.Div(
                                    [
                                        html.Button("Download Excel", id="btn-excel-country", className="btn-excel"),
                                        dcc.Download(id="download-excel-country"),
                                    ]
                                )
                            ],
                            id="cross-filter-options",
                            className="pretty_container",
                        ),
                        html.Div(
                            id='figure-country',
                            className="pretty_container",
                        ),
                    ],
                    className="row flex-display",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3("Sources rate table"),
                                create_chart_datatable(df_sources),
                                html.Div(
                                    [
                                        html.Button("Download Excel", id="btn-excel-source", className="btn-excel"),
                                        dcc.Download(id="download-excel-source"),
                                    ]
                                )
                            ],
                            id="cross-filter-options",
                            className="pretty_container",
                        ),
                        html.Div(
                            id='figure-source',
                            className="pretty_container",
                        ),
                    ],
                    className="row flex-display",
                ),

                html.Div(
                    [
                        html.H3("Publications dynamic"),
                        dcc.Graph(
                            figure=dict(
                                data=[
                                    dict(
                                        x=df_dinamic['Year'],
                                        y=df_dinamic['Number'],
                                        name='China',
                                        marker=dict(
                                            color='rgb(26, 118, 255)'
                                        )
                                    )
                                ],
                                layout=dict(
                                    margin=dict(l=40, r=80, t=20, b=30)
                                )
                            ),
                            style={'height': 300},
                            id='my-graph-example'
                        ),
                    ]
                ),
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
    Output('figure-author', "children"),
    Input('table-with-figure-author', "selected_rows"),
    Input('table-with-figure-author', "sort_by"))
def update_figure_authors(selected_rows, sort_by):
    return html.Div(
            [
                html.H3("Authors - Rate"),
                dcc.Graph(
                    figure=create_bar_chart_rate(df_authors, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
                html.H3("Authors - Number of docs"),
                dcc.Graph(
                    figure=create_bar_chart_docs_num(df_authors, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                )
            ],
    )

@app.callback(
    Output('figure-organization', "children"),
    Input('table-with-figure-organization', "selected_rows"),
    Input('table-with-figure-organization', "sort_by"))
def update_figure_organizations(selected_rows, sort_by):
    return html.Div(
            [
                html.H3("Organizations - Rate"),
                dcc.Graph(
                    figure=create_bar_chart_rate(df_organizations, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
                html.H3("Organizations - Number of docs"),
                dcc.Graph(
                    figure=create_bar_chart_docs_num(df_organizations, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
            ]
    )

@app.callback(
    Output('figure-funding', "children"),
    Input('table-with-figure-funding', "selected_rows"),
    Input('table-with-figure-funding', "sort_by"))
def update_figure_fundings(selected_rows, sort_by):
    return html.Div(
            [
                html.H3("Fundings - Rate"),
                dcc.Graph(
                    figure=create_bar_chart_rate(df_fundings, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
                html.H3("Fundings - Number of docs"),
                dcc.Graph(
                    figure=create_bar_chart_docs_num(df_fundings, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
            ]
    )

@app.callback(
    Output('figure-country', "children"),
    Input('table-with-figure-country', "selected_rows"),
    Input('table-with-figure-country', "sort_by"))
def update_figure_countries(selected_rows, sort_by):
    return html.Div(
            [
                html.H3("Countries - Rate"),
                dcc.Graph(
                    figure=create_bar_chart_rate(df_countries, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
                html.H3("Countries - Number of docs"),
                dcc.Graph(
                    figure=create_bar_chart_docs_num(df_countries, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
            ]
    )


@app.callback(
    Output('figure-source', "children"),
    Input('table-with-figure-source', "selected_rows"),
    Input('table-with-figure-source', "sort_by"))
def update_figure_sources(selected_rows, sort_by):
    return html.Div(
            [
                html.H3("Sources - Rate"),
                dcc.Graph(
                    figure=create_bar_chart_rate(df_sources, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
                html.H3("Sources - Number of docs"),
                dcc.Graph(
                    figure=create_bar_chart_docs_num(df_sources, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
            ]
    )


@app.callback(
    Output("download-excel-author", "data"),
    Input("btn-excel-author", "n_clicks"),
    State('table-with-figure-author', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, selected_rows):
    dff = df_authors.iloc[selected_rows]
    return dcc.send_data_frame(dff.to_excel, "authors_rate.xlsx")


@app.callback(
    Output("download-excel-organization", "data"),
    Input("btn-excel-organization", "n_clicks"),
    State('table-with-figure-organization', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, selected_rows):
    dff = df_organizations.iloc[selected_rows]
    return dcc.send_data_frame(dff.to_excel, "organizations_rate.xlsx")


@app.callback(
    Output("download-excel-funding", "data"),
    Input("btn-excel-funding", "n_clicks"),
    State('table-with-figure-funding', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, selected_rows):
    dff = df_fundings.iloc[selected_rows]
    return dcc.send_data_frame(dff.to_excel, "fundings_rate.xlsx")


@app.callback(
    Output("download-excel-country", "data"),
    Input("btn-excel-country", "n_clicks"),
    State('table-with-figure-country', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, selected_rows):
    dff = df_countries.iloc[selected_rows]
    return dcc.send_data_frame(dff.to_excel, "countries_rate.xlsx")


@app.callback(
    Output("download-excel-source", "data"),
    Input("btn-excel-source", "n_clicks"),
    State('table-with-figure-source', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, selected_rows):
    dff = df_sources.iloc[selected_rows]
    return dcc.send_data_frame(dff.to_excel, "sources_rate.xlsx")
