import plotly.graph_objects as go


def create_treemap_chart(df):
    words_dict = {}
    for _, row in df.iterrows():
        cell = row["keywords"].split("; ")
        for word in cell:
            if len(word) != 0:
                words_dict[word.lower()] = words_dict.get(word.lower(), 0) + 1
    words_dict = {k: v for k, v in sorted(words_dict.items(), key=lambda x: x[1], reverse=True)}
    dict_df = {"keywords": list(words_dict.keys()), "count": list(words_dict.values())}


    dv = dict_df["count"]
    dv.insert(0, 0)
    dk = dict_df["keywords"]
    dk.insert(0, "ключевые слова")
    par = ["ключевые слова" for _ in range(100)]
    par.insert(0, "")
    num_displayed_keywords = 20

    color_scale=[[0, 'white'], [0.1, 'rgb(240, 246, 253)'], [0.5, 'rgb(151, 174, 217)'], [0.7, 'rgb(45, 75, 151)'], [1, 'rgb(23, 45, 101)']]
    fig = go.Figure(go.Treemap(
                    values=dv[:num_displayed_keywords],
                    labels=dk[:num_displayed_keywords],
                    parents=par[:num_displayed_keywords],
                    marker_colorscale=color_scale,
                    textinfo="label+value",
                    textposition='middle center',
                    textfont=dict(size=20, family='HSE SemiBold')
                    ))
    fig.update_layout(margin=dict(t=20, l=20, r=20, b=20))
    return fig

