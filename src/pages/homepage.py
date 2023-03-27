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
                    id="btn-header",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H2("Данный проект представляет собой дашборд по ключевым центрам научных компетенций \
                                        России и мира в выбранных предметных областях."),

                                html.H2("В него включены 2 раздела: \
                                        общая информация по конкретной области и инфографика по наиболее цитируемым статьям по этой области. \
                                        Ниже представлено краткое описание каждого из разделов."),

                                html.H2("Для перехода на страницу с соответствующим разделом воспользуйтесь навигационной \
                                        панелью в верхней части страницы."),
                            ],
                            style={
                                'text-align': 'justify'
                            }
                        ),
                        dbc.Nav(
                            [
                                html.Div(
                                    [
                                        html.H3("Общая информация по научной области", id="chapter-title"),
                                        html.P("В данном разделе представлены таблицы и графики по рейтингам:"),
                                        html.Ul(
                                            [
                                                html.Li("авторов статей;"),
                                                html.Li("организаций, публикующих статьи;"),
                                                html.Li("спонсирующих организаций;"),
                                                html.Li("стран, в которых были опубликованы статьи;"),
                                                html.Li("научных журналов."),
                                            ]
                                        ),
                                        html.P("Также представлен график с динамикой публикаций по последним годам."),
                                        html.P("Доступны:"),
                                        html.Ul(
                                            [
                                                html.Li("выгрузка графиков в формате png (доступна справа сверху при наведении курсора на график);"),
                                                html.Li("сортировка каждого из столбцов таблиц и поиск по ним;"),
                                                html.Li("выгрузка таблиц (доступна при нажатии соответствующей кнопки над таблицей)."),
                                            ]
                                        ),
                                    ],
                                    className="pretty_container",
                                    style={
                                        'width': '50%',
                                        'text-align': 'justify',
                                        'font-size': '120%'
                                    }
                                ),
                                html.Div(
                                    [
                                        html.H3("Инфографика по наиболее цитируемым статьям", id="chapter-title"),
                                        html.P("В данном разделе представлены краткая версия таблицы с топ-2000 наиболее цитируемых статей и список \
                                                ключевых слов с количеством документов, которые содержат данные ключевые слова."),
                                        html.P("Также представлены круговые диаграммы по количеству следующих показателей:"),
                                        html.Ul(
                                            [
                                                html.Li("тип документа (например, статья, глава книги);"),
                                                html.Li("научные журналы;"),
                                                html.Li("публикаторы (например, Springer)."),
                                            ]
                                        ),
                                        html.P("Доступны:"),
                                        html.Ul(
                                            [
                                                html.Li("выгрузка графиков в формате png (доступна справа сверху при наведении курсора на график);"),
                                                html.Li("фильтрации данных по выбранным ключевым словам;"),
                                                html.Li("сортировка каждого из столбцов и поиск по ним;"),
                                                html.Li("выгрузка краткой версии таблицы (доступна при нажатии соответствующей кнопки над таблицей);"),
                                                html.Li("выгрузка полной версии таблицы (доступна при нажатии соответствующей кнопки над таблицей. Полная версия отличается от краткой наличием дополнительной информации, например, ISSN)."),
                                            ]
                                        ),
                                    ],
                                    className="pretty_container",
                                    style={
                                        'width': '50%',
                                        'text-align': 'justify',
                                        'font-size': '120%'
                                    }
                                ),
                            ],
                            className="row flex-display"
                        )
                    ],
                    style={
                        "padding": "10px",
                    }
                ),
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
    Output('btn-header', 'children'),
    Input('url', 'pathname'))
def create_header_button(pathname):
    id_btn_home = "button-header-current" if pathname == "/" else "button-header"
    id_btn_general_info = "button-header-current" if pathname == "/general_info" else "button-header"
    id_btn_top_cited = "button-header-current" if pathname == "/top_cited" else "button-header"

    return html.Div(
        [
            html.Div(
                [
                    html.A(html.Button('Начальная страница', className=id_btn_home), href='/'),
                    html.A(html.Button('Общая информация по научной области', className=id_btn_general_info), href='/general_info'),
                    html.A(html.Button('Инфографика по наиболее цитируемым статьям', className=id_btn_top_cited), href='/top_cited'),
                ],
                id="header-btn-flex"
            ),
            html.Hr()
        ]
    )


@app.callback(
    Output('left-column', 'style'),
    Input('url', 'pathname'))
def update_left_column(pathname):
    height = '100%'
    if pathname == "/general_info":
        height = 'calc(350px * 9 - 110px)'
    elif pathname == "/top_cited":
        height = 'calc(350px * 9 + 55px)'

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
        height = 'calc(350px * 9 - 110px)'
    elif pathname == "/top_cited":
        height = 'calc(350px * 9 + 55px)'

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
