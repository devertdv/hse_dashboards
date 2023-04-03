from dash import html, dcc
from dash.dependencies import Input, Output, State
from app import app
from src.components.get_fields import *
from src.components.create_bar_chart import *
from src.components.create_chart_datatable import *
from src.components.create_dynamics_chart import *
from src.components.create_left_column import *
from src.components.create_right_column import *
from src.components.read_files_authors import *
from src.components.read_files_countries import *
from src.components.read_files_fundings import *
from src.components.read_files_organizations import *
from src.components.read_files_pub_dynamic import *
from src.components.read_files_sources import *
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
                                    get_fields(),
                                    'Accounting',
                                    id='dropdown-fields',
                                    style={
                                        'font-family': 'HSE Font'
                                    }
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
                                        html.Div(
                                            id='authors-datatable'
                                        ),
                                    ],
                                    id="cross-filter-options",
                                    className="pretty_container container_chart_datatable",
                                ),
                                html.Div(
                                    id='figure-author',
                                    className="bar_chart"
                                ),
                                dcc.Store(id="authors-df"),
                                dcc.Store(id="authors-rows"),
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
                                        html.Div(
                                            id='organizations-datatable'
                                        ),
                                    ],
                                    id="cross-filter-options",
                                    className="pretty_container container_chart_datatable",
                                ),
                                html.Div(
                                    id='figure-organization',
                                    className="bar_chart"
                                ),
                                dcc.Store(id="organizations-df"),
                                dcc.Store(id="organizations-rows"),
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
                                        html.Div(
                                            id='fundings-datatable'
                                        ),
                                    ],
                                    id="cross-filter-options",
                                    className="pretty_container container_chart_datatable",
                                ),
                                html.Div(
                                    id='figure-funding',
                                    className="bar_chart"
                                ),
                                dcc.Store(id="fundings-df"),
                                dcc.Store(id="fundings-rows"),
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
                                        html.Div(
                                            id='countries-datatable'
                                        ),
                                    ],
                                    id="cross-filter-options",
                                    className="pretty_container container_chart_datatable",
                                ),
                                html.Div(
                                    id='figure-country',
                                    className="bar_chart"
                                ),
                                dcc.Store(id="countries-df"),
                                dcc.Store(id="countries-rows"),
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
                                        html.Div(
                                            id='sources-datatable'
                                        ),
                                    ],
                                    id="cross-filter-options",
                                    className="pretty_container container_chart_datatable",
                                ),
                                html.Div(
                                    id='figure-source',
                                    className="bar_chart"
                                ),
                                dcc.Store(id="sources-df"),
                                dcc.Store(id="sources-rows"),
                            ],
                            className="row",
                        ),

                        html.Div(
                            [
                                html.Div(
                                    html.H3("Динамика публикаций")
                                ),
                                html.Div(
                                    id="pub_dynamics"
                                )
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


# callbacks read_files


@app.callback(
    Output('authors-df', 'data'),
    Input('dropdown-fields', 'value'))
def upload_files_authors(value):
    df = read_files_authors(value)
    return df.to_json(date_format='iso')


@app.callback(
    Output('organizations-df', 'data'),
    Input('dropdown-fields', 'value'))
def upload_files_organizations(value):
    df = read_files_organizations(value)
    return df.to_json(date_format='iso')


@app.callback(
    Output('fundings-df', 'data'),
    Input('dropdown-fields', 'value'))
def upload_files_fundings(value):
    df = read_files_fundings(value)
    return df.to_json(date_format='iso')


@app.callback(
    Output('countries-df', 'data'),
    Input('dropdown-fields', 'value'))
def upload_files_countries(value):
    df = read_files_countries(value)
    return df.to_json(date_format='iso')


@app.callback(
    Output('sources-df', 'data'),
    Input('dropdown-fields', 'value'))
def upload_files_sources(value):
    df = read_files_sources(value)
    return df.to_json(date_format='iso')


# callbacks create_table


@app.callback(
    Output('authors-datatable', 'children'),
    Input('authors-df', 'data'))
def update_authors_datatable(data):
    df = pd.read_json(data)
    return create_chart_datatable(df)


@app.callback(
    Output('organizations-datatable', 'children'),
    Input('organizations-df', 'data'))
def update_organizations_datatable(data):
    df = pd.read_json(data)
    return create_chart_datatable(df)


@app.callback(
    Output('fundings-datatable', 'children'),
    Input('fundings-df', 'data'))
def update_fundings_datatable(data):
    df = pd.read_json(data)
    return create_chart_datatable(df)


@app.callback(
    Output('countries-datatable', 'children'),
    Input('countries-df', 'data'))
def update_countries_datatable(data):
    df = pd.read_json(data)
    return create_chart_datatable(df)


@app.callback(
    Output('sources-datatable', 'children'),
    Input('sources-df', 'data'))
def update_sources_datatable(data):
    df = pd.read_json(data)
    return create_chart_datatable(df)


# callbacks create_chart


@app.callback(
    Output('figure-author', "children"),
    Input('authors-df', 'data'),
    Input('table-with-figure-author', "selected_rows"),
    Input('table-with-figure-author', "sort_by"),
    prevent_initial_call=True,)
def update_figure_authors(data, selected_rows, sort_by):
    df = pd.read_json(data)
    return html.Div(
        [
            html.H3("График рейтинга авторов"),
            dcc.Graph(
                figure=create_bar_chart(df, selected_rows, sort_by),
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
    Input('organizations-df', 'data'),
    Input('table-with-figure-organization', "selected_rows"),
    Input('table-with-figure-organization', "sort_by"))
def update_figure_organizations(data, selected_rows, sort_by):
    df = pd.read_json(data)
    return html.Div(
        [
            html.H3("График рейтинга публикаторов"),
            dcc.Graph(
                figure=create_bar_chart(df, selected_rows, sort_by),
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
    Input('fundings-df', 'data'),
    Input('table-with-figure-funding', "selected_rows"),
    Input('table-with-figure-funding', "sort_by"))
def update_figure_fundings(data, selected_rows, sort_by):
    df = pd.read_json(data)
    return html.Div(
        [
            html.H3("График рейтинга спонсоров"),
            dcc.Graph(
                figure=create_bar_chart(df, selected_rows, sort_by),
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
    Input('countries-df', 'data'),
    Input('table-with-figure-country', "selected_rows"),
    Input('table-with-figure-country', "sort_by"))
def update_figure_countries(data, selected_rows, sort_by):
    df = pd.read_json(data)
    return html.Div(
        [
            html.H3("График рейтинга стран"),
            dcc.Graph(
                figure=create_bar_chart(df, selected_rows, sort_by),
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
    Input('sources-df', 'data'),
    Input('table-with-figure-source', "selected_rows"),
    Input('table-with-figure-source', "sort_by"))
def update_figure_sources(data, selected_rows, sort_by):
    df = pd.read_json(data)
    return html.Div(
        [
            html.H3("График рейтинга журналов"),
            dcc.Graph(
                figure=create_bar_chart(df, selected_rows, sort_by),
                style={
                    'overflowY': 'scroll',
                    'height': 350,
                    'width': '100%'
                }
            ),
        ],
        className="pretty_container",
    )


# callbacks download_excel


@app.callback(
    Output("download-excel-author", "data"),
    Input("btn-excel-author", "n_clicks"),
    State('dropdown-fields', 'value'),
    State('authors-df', 'data'),
    State('table-with-figure-author', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, field, data, selected_rows):
    df = pd.read_json(data)
    dff = df.iloc[selected_rows]
    dff = dff.sort_values(by=[dff.columns[1]], ascending=False)
    return dcc.send_data_frame(dff.to_excel, f"{field} authors_rate.xlsx")


@app.callback(
    Output("download-excel-organization", "data"),
    Input("btn-excel-organization", "n_clicks"),
    State('dropdown-fields', 'value'),
    State('organizations-df', 'data'),
    State('table-with-figure-organization', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, field, data, selected_rows):
    df = pd.read_json(data)
    dff = df.iloc[selected_rows]
    dff = dff.sort_values(by=[dff.columns[1]], ascending=False)
    return dcc.send_data_frame(dff.to_excel, f"{field} organizations_rate.xlsx")


@app.callback(
    Output("download-excel-funding", "data"),
    Input("btn-excel-funding", "n_clicks"),
    State('dropdown-fields', 'value'),
    State('fundings-df', 'data'),
    State('table-with-figure-funding', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, field, data, selected_rows):
    df = pd.read_json(data)
    dff = df.iloc[selected_rows]
    dff = dff.sort_values(by=[dff.columns[1]], ascending=False)
    return dcc.send_data_frame(dff.to_excel, f"{field} fundings_rate.xlsx")


@app.callback(
    Output("download-excel-country", "data"),
    Input("btn-excel-country", "n_clicks"),
    State('dropdown-fields', 'value'),
    State('countries-df', 'data'),
    State('table-with-figure-country', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, field, data, selected_rows):
    df = pd.read_json(data)
    dff = df.iloc[selected_rows]
    dff = dff.sort_values(by=[dff.columns[1]], ascending=False)
    return dcc.send_data_frame(dff.to_excel, f"{field} countries_rate.xlsx")


@app.callback(
    Output("download-excel-source", "data"),
    Input("btn-excel-source", "n_clicks"),
    State('dropdown-fields', 'value'),
    State('sources-df', 'data'),
    State('table-with-figure-source', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, field, data, selected_rows):
    df = pd.read_json(data)
    dff = df.iloc[selected_rows]
    dff = dff.sort_values(by=[dff.columns[1]], ascending=False)
    return dcc.send_data_frame(dff.to_excel, f"{field} sources_rate.xlsx")


# callback pub_dynamics


@app.callback(
    Output('pub_dynamics', 'children'),
    Input('dropdown-fields', 'value'))
def update_dynamics_chart(value):
    df = read_files_pub_dynamic(value)
    return create_dynamics_chart(df)
