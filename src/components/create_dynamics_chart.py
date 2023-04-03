from dash import dcc


def create_dynamics_chart(df):
    return dcc.Graph(
        figure=dict(
            data=[
                dict(
                    x=df['Year'],
                    y=df['Number'],
                    marker=dict(
                        color='rgb(23, 45, 101)'
                    )
                )
            ],
            layout=dict(
                margin=dict(l=40, r=0, t=20, b=30),
                traces=dict(textposition='top center'),
                xaxis=dict(dtick=1),
                font=dict(family='HSE Font'),
            ),
        ),
        style={
            'height': 350,
        },
        id='my-graph-example',
    )