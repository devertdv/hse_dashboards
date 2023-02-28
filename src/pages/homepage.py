from dash import html
import dash_bootstrap_components as dbc


homepage_layout = html.Div(
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
                        dbc.NavLink("Инфографика по наиболее релевантным статьям", href="/top_relevant", active="exact"),
                        html.P("Тут тоже какой то небольшой текст про то, что будет в разделе \"Инфографика по наиболее релевантным статьям\"")
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
)
