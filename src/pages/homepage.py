from app import app
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


homepage_layout = html.Div(
    [
        html.Div(
            [
            ],
            id="btn-header"
        ),
        html.Div(
            [
                html.H1("Welcome"),
                html.H2("Некоторая приветственная речь и объяснение, как что и куда жмать"),
                dbc.Nav(
                    [
                        html.Div(
                            [
                                dbc.NavLink("Общая информация по научной области", href="/general_info", active="exact"),
                                html.P("Тут тоже какой то небольшой текст про то, что будет в разделе \"Общая информация по научной области\"")
                            ],
                            className="pretty_container",
                        ),
                        html.Div(
                            [
                                dbc.NavLink("Инфографика по наиболее цитируемым статьям", href="/top_cited", active="exact"),
                                html.P("Тут тоже какой то небольшой текст про то, что будет в разделе \"Инфографика по наиболее цитируемым статьям\"")
                            ],
                            className="pretty_container",
                        ),
                    ],
                    className="row flex-display"
                )
            ],
            style={
                "margin": "auto",
                "width": "50%",
                "padding": "10px",
            }
        ),
    ],
)


@app.callback(
    Output('btn-header', 'children'),
    Input('url', 'pathname'))
def create_header_button(pathname):
    id_btn_home = "button-header-current" if pathname == "/" else "button-header"
    id_btn_general_info = "button-header-current" if pathname == "/general_info" else "button-header"
    id_btn_top_cited = "button-header-current" if pathname == "/top_cited" else "button-header"

    return html.Div(
        [
            html.A(html.Button('Начальная страница', className=id_btn_home), href='/'),
            html.A(html.Button('Общая информация по научной области', className=id_btn_general_info), href='/general_info'),
            html.A(html.Button('Инфографика по наиболее цитируемым статьям', className=id_btn_top_cited), href='/top_cited')
        ]
    )
