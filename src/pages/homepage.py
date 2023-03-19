from app import app
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from src.components.create_left_column import *
from src.components.create_right_column import *


homepage_layout = html.Div(
    [
        create_left_column(),
        html.Div(
            [
                html.Div(
                    [],
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
            style={
                "margin-left": "12%",
                "margin-right": "12%",
                "margin-right": "2rem",
                "padding": "2rem 1rem",
            }
        ),
        create_right_column(),
    ]
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


@app.callback(
    Output('left-column', 'style'),
    Input('url', 'pathname'))
def update_right_column(pathname):
    height = '100%'
    if pathname == "/general_info":
        height = 'calc(350px * 15 + 120px)'
    elif pathname == "/top_cited":
        height = 'calc(350px * 9 + 90px)'

    return {
        'position': 'absolute',
        'top': 0,
        'left': 0,
        'bottom': 0,
        'width': '10%',
        'height': height,
        'background-color': '#192f67',
        'box-shadow': 'inset 0px 0px 0px 5px rgba(0, 0, 0, 0)',
    }


@app.callback(
    Output('right-column', 'style'),
    Input('url', 'pathname'))
def update_right_column(pathname):
    height = '100%'
    if pathname == "/general_info":
        height = 'calc(350px * 15 + 120px)'
    elif pathname == "/top_cited":
        height = 'calc(350px * 9 + 90px)'

    return {
        'position': 'absolute',
        'top': 0,
        'right': 0,
        'bottom': 0,
        'width': '10%',
        'height': height,
        'background-color': '#192f67',
        'box-shadow': 'inset 0px 0px 0px 5px rgba(0, 0, 0, 0)',
    }
