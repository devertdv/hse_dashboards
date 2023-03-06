import plotly.graph_objects as go

def create_pie_chart(df, argument, click_data):
    select_rows = []
    if click_data is not None and "entry" in click_data["points"][0] and click_data["points"][0]["entry"] != \
            click_data["points"][0]["label"]:
        keyword = click_data["points"][0]["label"]
        for idx, row in df.iterrows():
            cell = row["Author Keywords"].split("; ")
            if keyword in cell:
                select_rows.append(idx)
    else:
        select_rows = [i for i in range(df.shape[0])]
    dff = df.iloc[select_rows]

    labels = []
    values = []
    for idx, name in enumerate(dff[argument].value_counts().index.tolist()):
        labels.append(name)
        values.append(dff[argument].value_counts()[idx])


    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    fig.update_layout(margin=dict(t=3, l=3, r=3, b=3))
    return fig

