import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

from src.components.bar_chart import *
from src.components.big_table import *
from src.components.read_files import *
from src.components.table_chart import *
from src.components.treemap_chart import *

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div([
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
                                html.Button("Download CSV", id="btn-csv-author", className="btn-csv"),
                                dcc.Download(id="download-csv-author"),
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
                                html.Button("Download CSV", id="btn-csv-organization", className="btn-csv"),
                                dcc.Download(id="download-csv-organization"),
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
                                html.Button("Download CSV", id="btn-csv-funding", className="btn-csv"),
                                dcc.Download(id="download-csv-funding"),
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
                                html.Button("Download CSV", id="btn-csv-country", className="btn-csv"),
                                dcc.Download(id="download-csv-country"),
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
                                html.Button("Download CSV", id="btn-csv-source", className="btn-csv"),
                                dcc.Download(id="download-csv-source"),
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
                html.H3("Publications dinamic"),
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
                html.H3("Authors rate bar chart"),
                dcc.Graph(
                    figure=create_bar_chart(df_authors, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
            ]
    )

@app.callback(
    Output('figure-organization', "children"),
    Input('table-with-figure-organization', "selected_rows"),
    Input('table-with-figure-organization', "sort_by"))
def update_figure_organizations(selected_rows, sort_by):
    return html.Div(
            [
                html.H3("Organizations rate bar chart"),
                dcc.Graph(
                    figure=create_bar_chart(df_organizations, selected_rows, sort_by),
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
                html.H3("Fundings rate bar chart"),
                dcc.Graph(
                    figure=create_bar_chart(df_fundings, selected_rows, sort_by),
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
                html.H3("Countries rate bar chart"),
                dcc.Graph(
                    figure=create_bar_chart(df_countries, selected_rows, sort_by),
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
                html.H3("Sources rate bar chart"),
                dcc.Graph(
                    figure=create_bar_chart(df_sources, selected_rows, sort_by),
                    style={
                        'overflowY': 'scroll',
                        'height': 350,
                        'width': 650
                    }
                ),
            ]
    )


@app.callback(
    Output("download-csv-author", "data"),
    Input("btn-csv-author", "n_clicks"),
    State('table-with-figure-author', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, selected_rows):
    dff = df_authors.iloc[selected_rows]
    return dcc.send_data_frame(dff.to_csv, "authors_rate.csv")


@app.callback(
    Output("download-csv-organization", "data"),
    Input("btn-csv-organization", "n_clicks"),
    State('table-with-figure-organization', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, selected_rows):
    dff = df_organizations.iloc[selected_rows]
    return dcc.send_data_frame(dff.to_csv, "organizations_rate.csv")


@app.callback(
    Output("download-csv-funding", "data"),
    Input("btn-csv-funding", "n_clicks"),
    State('table-with-figure-funding', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, selected_rows):
    dff = df_fundings.iloc[selected_rows]
    return dcc.send_data_frame(dff.to_csv, "fundings_rate.csv")


@app.callback(
    Output("download-csv-country", "data"),
    Input("btn-csv-country", "n_clicks"),
    State('table-with-figure-country', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, selected_rows):
    dff = df_countries.iloc[selected_rows]
    return dcc.send_data_frame(dff.to_csv, "countries_rate.csv")


@app.callback(
    Output("download-csv-source", "data"),
    Input("btn-csv-source", "n_clicks"),
    State('table-with-figure-source', "selected_rows"),
    prevent_initial_call=True,
)
def func(n_clicks, selected_rows):
    dff = df_sources.iloc[selected_rows]
    return dcc.send_data_frame(dff.to_csv, "sources_rate.csv")


@app.callback(
    Output("big-table", "children"),
    Input("treemap-chart", "clickData")
)
def update_big_table(clickData):
    return create_big_table(df_big_table, clickData)


if __name__ == '__main__':
    app.run_server(debug=True)