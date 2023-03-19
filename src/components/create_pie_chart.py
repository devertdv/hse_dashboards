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


    blue_colors = ["F7FBFF","F6FAFE","F5F9FD","F4F8FD","F3F7FC","F2F7FC","F1F6FB","F0F5FA","EFF4FA","EEF3F9","EDF3F9","ECF2F8","EBF1F8","EAF0F7","E9EFF6","E8EFF6","E8EEF5","E7EDF5","E6ECF4","E5EBF3","E4EBF3","E3EAF2","E2E9F2","E1E8F1","E0E7F1","DFE7F0","DEE6EF","DDE5EF","DCE4EE","DBE3EE","DAE3ED","D9E2ED","D9E1EC","D8E0EB","D7DFEB","D6DFEA","D5DEEA","D4DDE9","D3DCE8","D2DBE8","D1DBE7","D0DAE7","CFD9E6","CED8E6","CDD7E5","CCD7E4","CBD6E4","CAD5E3","CAD4E3","C9D3E2","C8D3E1","C7D2E1","C6D1E0","C5D0E0","C4D0DF","C3CFDF","C2CEDE","C1CDDD","C0CCDD","BFCCDC","BECBDC","BDCADB","BCC9DB","BBC8DA","BBC8D9","BAC7D9","B9C6D8","B8C5D8","B7C4D7","B6C4D6","B5C3D6","B4C2D5","B3C1D5","B2C0D4","B1C0D4","B0BFD3","AFBED2","AEBDD2","ADBCD1","ACBCD1","ACBBD0","ABBACF","AAB9CF","A9B8CE","A8B8CE","A7B7CD","A6B6CD","A5B5CC","A4B4CB","A3B4CB","A2B3CA","A1B2CA","A0B1C9","9FB0C9","9EB0C8","9DAFC7","9DAEC7","9CADC6","9BACC6","9AACC5","99ABC4","98AAC4","97A9C3","96A9C3","95A8C2","94A7C2","93A6C1","92A5C0","91A5C0","90A4BF","8FA3BF","8EA2BE","8EA1BD","8DA1BD","8CA0BC","8B9FBC","8A9EBB","899DBB","889DBA","879CB9","869BB9","859AB8","8499B8","8399B7","8298B7","8197B6","8096B5","7F95B5","7F95B4","7E94B4","7D93B3","7C92B2","7B91B2","7A91B1","7990B1","788FB0","778EB0","768DAF","758DAE","748CAE","738BAD","728AAD","7189AC","7089AC","7088AB","6F87AA","6E86AA","6D85A9","6C85A9","6B84A8","6A83A7","6982A7","6881A6","6781A6","6680A5","657FA5","647EA4","637EA3","627DA3","617CA2","617BA2","607AA1","5F7AA0","5E79A0","5D789F","5C779F","5B769E","5A769E","59759D","58749C","57739C","56729B","55729B","54719A","53709A","526F99","526E98","516E98","506D97","4F6C97","4E6B96","4D6A95","4C6A95","4B6994","4A6894","496793","486693","476692","466591","456491","446390","436290","43628F","42618E","41608E","405F8D","3F5E8D","3E5E8C","3D5D8C","3C5C8B","3B5B8A","3A5A8A","395A89","385989","375888","365788","355787","345686","345586","335485","325385","315384","305283","2F5183","2E5082","2D4F82","2C4F81","2B4E81","2A4D80","294C7F","284B7F","274B7E","264A7E","25497D","25487C","24477C","23477B","22467B","21457A","20447A","1F4379","1E4378","1D4278","1C4177","1B4077","1A3F76","193F76","183E75","173D74","163C74","163B73","153B73","143A72","133971","123871","113770","103770","0F366F","0E356F","0D346E","0C336D","0B336D","0A326C","09316C","08306B","08306B"]
    blue_colors = blue_colors[::12]
    blue_colors.reverse()

    color_scale_bright = ['#192f67', '#1c326a', '#1e3b84', '#234499', '#284eae',
                        '#3358BF', '#4165C9', '#5072D0', '#6284db', '#6c8cde',
                        '#819de2', '#8ca5e5', '#96ade7', '#a1b5ea', '#abbdec',
                        '#b6c6ee', '#cbd6f3', '#d5def5', '#eaeffa', '#f5f7fd']
    

    fig = go.Figure(data=[go.Pie(labels=labels,
                                values=values,
                                marker_colors=color_scale_bright[::len(color_scale_bright) // len(labels)])])
    fig.update_traces(textposition='inside')
    fig.update_layout(
        uniformtext_minsize=12,
        uniformtext_mode='hide',
        margin=dict(t=3, l=3, r=3, b=3)
    )
    return fig

