from dash import dash_table

def create_chart_datatable(df):

    df = df.sort_values(by=[df.columns[1], df.columns[0]], ascending=[False, True])

    return dash_table.DataTable(
                id=f'table-with-figure-{df.columns[0].lower()}',
                data=df.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df.columns],

                fixed_rows={'headers': True},
                sort_action="native",
                sort_mode="single",
                sort_by=[],
                editable=True,
                row_selectable='multi',
                selected_rows=[i for i in range(df.shape[0])],

                style_table={
                    'height': 800,
                },
                style_cell={
                    'minWidth': 200,
                    'width': 200,
                    'maxWidth': 200,
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                },
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                },
    )