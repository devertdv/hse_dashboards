import plotly.graph_objects as go
import textwrap as tw


def create_bar_chart(df, selected_rows=[], sort_by=[]):
    dff = df.iloc[selected_rows]
    dff.loc[:, dff.columns[0]] = dff.loc[:, dff.columns[0]].apply(lambda x: "<br>".join(tw.wrap(x, width=20)))

    if sort_by:
        if sort_by[0][list(sort_by[0].keys())[0]] == dff.columns[0]:
            if sort_by[0][list(sort_by[0].keys())[1]] == 'asc':
                dff = dff.sort_values(by=[dff.columns[0]], ascending=False)
            elif sort_by[0][list(sort_by[0].keys())[1]] == 'desc':
                dff = dff.sort_values(by=[dff.columns[0]], ascending=True)
        elif sort_by[0][list(sort_by[0].keys())[0]] == dff.columns[1]:
            if sort_by[0][list(sort_by[0].keys())[1]] == 'asc':
                dff = dff.sort_values(by=[dff.columns[1], dff.columns[0]], ascending=[False, False])
            elif sort_by[0][list(sort_by[0].keys())[1]] == 'desc':
                dff = dff.sort_values(by=[dff.columns[1], dff.columns[0]], ascending=[True, False])
        elif sort_by[0][list(sort_by[0].keys())[0]] == dff.columns[2]:
            if sort_by[0][list(sort_by[0].keys())[1]] == 'asc':
                dff = dff.sort_values(by=[dff.columns[2], dff.columns[1], dff.columns[0]], ascending=[False, True, False])
            elif sort_by[0][list(sort_by[0].keys())[1]] == 'desc':
                dff = dff.sort_values(by=[dff.columns[2], dff.columns[1], dff.columns[0]], ascending=[True, True, False])
    else:    
        dff = dff.sort_values(by=[dff.columns[1]], ascending=True)

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
    fig.update_traces(marker_color="rgb(23, 45, 101)")
    fig.update_layout(
        font_family='HSE SemiBold',
        font_size=14,
        yaxis={"categoryorder":"trace"},
        xaxis_title=None,
        yaxis_title=None,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=dff.shape[0]*70,
        width=670,
        margin=dict(l=20, r=20, t=20, b=20),
    )

    return fig
