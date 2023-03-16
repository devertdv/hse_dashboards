import plotly.graph_objects as go

def create_pie_chart(df, argument):

    labels = []
    values = []
    for idx, name in enumerate(df[argument].value_counts().index.tolist()):
        labels.append(name)
        values.append(df[argument].value_counts()[idx])


    blue_colors = ['midnightblue', 'navy', 'darkblue', 'mediumblue', 'blue', 'b',
                    'royalblue', 'cornflowerblue', 'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'aliceblue',
                    'lightcyan', 'azure', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white',
                    'white','white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white',
                    'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white',
                    'white', 'white', 'white', 'white', 'white','white', 'white', 'white', 'white', 'white']
    fig = go.Figure(data=[go.Pie(labels=labels, values=values,  marker_colors=blue_colors)])
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    fig.update_layout(margin=dict(t=3, l=3, r=3, b=3))
    return fig

