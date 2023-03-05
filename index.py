from dash import html, dcc
from dash.dependencies import Input, Output

from app import app
from src.pages import homepage, general_info, top_relevant

url_content_layout = html.Div(
    [
    dcc.Location(id="url", refresh=False),
    html.Div(id="output-div")
    ]
)

app.layout = url_content_layout

app.validation_layout = html.Div(
    [
    url_content_layout,
    homepage.homepage_layout,
    general_info.general_info_layout,
    top_relevant.top_relevant_layout
    ]
)


@app.callback(
        Output(component_id="output-div",component_property="children"),
        Input(component_id="url",component_property="pathname"))
def update_output_div(pathname):
    if pathname == "/":
        return homepage.homepage_layout
    elif pathname == "/general_info":
        return general_info.general_info_layout
    elif pathname == "/top_cited":
        return top_relevant.top_relevant_layout
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)
