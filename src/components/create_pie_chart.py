import plotly.graph_objects as go

def create_pie_chart(df, column):

    labels_values = {}

    all_values = df[column].shape[0]
    min_percentage = 0.015
    value_others = 0
    for idx, name in enumerate(df[column].value_counts().index.tolist()):
        cur_value = df[column].value_counts()[idx]
        if cur_value / all_values < min_percentage:
            value_others += cur_value
        else:
            labels_values[name] = cur_value
    if value_others != 0:
        labels_values["others"] = value_others
    labels_values = {k: v for k, v in sorted(labels_values.items(), key=lambda item: item[1], reverse=True)}
    labels = list(labels_values.keys())
    values = list(labels_values.values())


    blue_colors = ['midnightblue', 'navy', 'darkblue', 'mediumblue', 'blue', 'b',
                    'royalblue', 'cornflowerblue', 'dodgerblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'aliceblue',
                    'lightcyan', 'azure', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white',
                    'white','white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white',
                    'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white',
                    'white', 'white', 'white', 'white', 'white','white', 'white', 'white', 'white', 'white']
    fig = go.Figure(data=[go.Pie(labels=labels,
                                values=values,
                                marker_colors=blue_colors)])
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    fig.update_layout(margin=dict(t=3, l=3, r=3, b=3))
    return fig

