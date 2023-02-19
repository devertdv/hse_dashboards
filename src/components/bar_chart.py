import plotly.graph_objects as go
from src.components.read_files import *

def create_bar_chart(df, selected_rows=[]):

    dff = df.iloc[selected_rows]

    fig = go.Figure(
        data=[go.Bar(
            y=dff[dff.columns[0]],
            x=dff[dff.columns[1]],
            text=dff[dff.columns[1]],
            orientation='h'
        )],
        layout={
            'xaxis': {'title': dff.columns[1], 'visible': False, 'showticklabels': False},

            'yaxis': {'title': dff.columns[0], 'visible': True, 'showticklabels': True},
        }
    )
    fig.update_layout(
        yaxis={"categoryorder":"total ascending"},
        xaxis_title=None,
        yaxis_title=None,
        template="plotly_white",
        height=dff.shape[0]*30,
        width=600,
        margin=dict(l=20, r=0, t=0, b=10),
    )

    return fig