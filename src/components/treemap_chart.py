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
    dv.insert(0, "count")

    dk = dict_df["keywords"]
    dk.insert(0, "keywords")

    par = ["keywords" for _ in range(100)]
    par.insert(0, "")


    fig = go.Figure(go.Treemap(
                    values=dv[0:20],
                    labels=dk[0:20],
                    textinfo="label+value",
                    parents=par,
                    root_color="snow",
                    marker_colorscale='blues',
                    textposition='middle center',
                    textfont=dict(size=20)
                    ))
    fig.update_layout(margin=dict(t=20, l=20, r=20, b=20))
    return fig

