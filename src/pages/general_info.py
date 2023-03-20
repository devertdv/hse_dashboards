from dash import html, dcc
from dash.dependencies import Input, Output, State
from app import app
from src.components.create_bar_chart import *
from src.components.create_chart_datatable import *
from src.components.create_dynamics_chart import *
from src.components.create_left_column import *
from src.components.create_right_column import *
from src.components.select_rows_big_table import *


general_info_layout = html.Div(
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
                    ],
                ),

                html.Div(
                    [
                        html.Div(html.H2("Общая информация по научной области")),
                        html.Div(
                            [
                                html.P('Выберите научную область'),
                                dcc.Dropdown(
                                    {'psy': 'Psychology', 'soft': 'Software', 'surg': 'Surgery'},
                                    'psy',
                                    id='clientside-graph-indicator'
                                )
                            ],
                        ),

                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H3("Таблица рейтинга авторов"),
                                                html.Div(
                                                    [
                                                        html.Button("Скачать Excel", id="btn-excel-author", className="btn-excel"),
                                                        dcc.Download(id="download-excel-author"),
                                                    ]
                                                )
                                            ],
                                            className="row-chart-datatable",
                                        ),
                                        create_chart_datatable(df_authors),
                                    ],
                                    id="cross-filter-options",
                                    className="pretty_container container_chart_datatable",
                                ),
                                html.Div(
                                    id='figure-author',
                                    className="bar_chart"
                                ),
                            ],
                            className="row flex-display",
                        ),

                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H3("Таблица рейтинга публикаторов"),
                                                html.Div(
                                                    [
                                                        html.Button("Скачать Excel", id="btn-excel-organization", className="btn-excel"),
                                                        dcc.Download(id="download-excel-organization"),
                                                    ]
                                                )
                                            ],
                                            className="row-chart-datatable",
                                        ),
                                        create_chart_datatable(df_organizations),
                                        
                                    ],
                                    id="cross-filter-options",
                                    className="pretty_container container_chart_datatable",
                                ),
                                html.Div(
                                    id='figure-organization',
                                    className="bar_chart"
                                ),
                            ],
                            className="row flex-display",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H3("Таблица рейтинга спонсоров"),
                                                html.Div(
                                                    [
                                                        html.Button("Скачать Excel", id="btn-excel-funding", className="btn-excel"),
                                                        dcc.Download(id="download-excel-funding"),
                                                    ]
                                                )
                                            ],
                                            className="row-chart-datatable",
                                        ),
                                        create_chart_datatable(df_fundings),
                                    ],
                                    id="cross-filter-options",
                                    className="pretty_container container_chart_datatable",
                                ),
                                html.Div(
                                    id='figure-funding',
                                    className="bar_chart"
                                ),
                            ],
                            className="row flex-display",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H3("Таблица рейтинга стран"),
                                                html.Div(
                                                    [
                                                        html.Button("Скачать Excel", id="btn-excel-country", className="btn-excel"),
                                                        dcc.Download(id="download-excel-country"),
                                                    ]
                                                )
                                            ],
                                            className="row-chart-datatable",
                                        ),
                                        create_chart_datatable(df_countries),
                                    ],
                                    id="cross-filter-options",
                                    className="pretty_container container_chart_datatable",
                                ),
                                html.Div(
                                    id='figure-country',
                                    className="bar_chart"
                                ),
                            ],
                            className="row flex-display",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H3("Таблица рейтинга журналов"),
                                                html.Div(
                                                    [
                                                        html.Button("Скачать Excel", id="btn-excel-source", className="btn-excel"),
                                                        dcc.Download(id="download-excel-source"),
                                                    ]
                                                )
                                            ],
                                            className="row-chart-datatable",
                                        ),
                                        create_chart_datatable(df_sources),
                                    ],
                                    id="cross-filter-options",
                                    className="pretty_container container_chart_datatable",
                                ),
                                html.Div(
                                    id='figure-source',
                                    className="bar_chart"
                                ),
                            ],
                            className="row",
                        ),

                        html.Div(
                            [
                                html.H3("Динамика публикаций"),
                                create_dynamics_chart(df_dynamics),
                            ],
                            className="pretty_container",
                        ),
                    ],
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


# callbacks


@app.callback(
    Output('figure-author', "children"),
    Input('table-with-figure-author', "selected_rows"),
    Input('table-with-figure-author', "sort_by"))
def update_figure_authors(selected_rows, sort_by):
    return html.Div(
        [
            html.H3("График рейтинга авторов"),
            dcc.Graph(
                figure=create_bar_chart(df_authors, selected_rows, sort_by),
                style={
                    'overflowY': 'scroll',
                    'height': 350,
                    'width': '100%'
                }
            ),
        ],
        className="pretty_container",
    )

@app.callback(
    Output('figure-organization', "children"),
    Input('table-with-figure-organization', "selected_rows"),
    Input('table-with-figure-organization', "sort_by"))
def update_figure_organizations(selected_rows, sort_by):
    return html.Div(
        [
            html.H3("График рейтинга публикаторов"),
            dcc.Graph(
                figure=create_bar_chart(df_organizations, selected_rows, sort_by),
                style={
                    'overflowY': 'scroll',
                    'height': 350,
                    'width': '100%'
                }
            ),
        ],
        className="pretty_container",
    )

@app.callback(
    Output('figure-funding', "children"),
    Input('table-with-figure-funding', "selected_rows"),
    Input('table-with-figure-funding', "sort_by"))
def update_figure_fundings(selected_rows, sort_by):
    return html.Div(
        [
            html.H3("График рейтинга спонсоров"),
            dcc.Graph(
                figure=create_bar_chart(df_fundings, selected_rows, sort_by),
                style={
                    'overflowY': 'scroll',
                    'height': 350,
                    'width': '100%'
                }
            ),
        ],
        className="pretty_container",
    )

@app.callback(
    Output('figure-country', "children"),
    Input('table-with-figure-country', "selected_rows"),
    Input('table-with-figure-country', "sort_by"))
def update_figure_countries(selected_rows, sort_by):
    return html.Div(
        [
            html.H3("График рейтинга стран"),
            dcc.Graph(
                figure=create_bar_chart(df_countries, selected_rows, sort_by),
                style={
                    'overflowY': 'scroll',
                    'height': 350,
                    'width': '100%'
                }
            ),
        ],
        className="pretty_container",
    )


@app.callback(
    Output('figure-source', "children"),
    Input('table-with-figure-source', "selected_rows"),
    Input('table-with-figure-source', "sort_by"))
def update_figure_sources(selected_rows, sort_by):
    return html.Div(
        [
            html.H3("График рейтинга журналов"),
            dcc.Graph(
                figure=create_bar_chart(df_sources, selected_rows, sort_by),
                style={
                    'overflowY': 'scroll',
                    'height': 350,
                    'width': '100%'
                }
            ),
        ],
        className="pretty_container",
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
