from dash import dash_table

def create_big_table(df, select_rows):

    return dash_table.DataTable(
                        data=df.to_dict('records'),
                        columns=[{'id': c, 'name': c} for c in df.columns],

                        fixed_rows={'headers': True},
                        sort_action="native",
                        sort_mode="single",
                        sort_by=[],
                        editable=True,
                        filter_action="native",
                        row_selectable='multi',
                        selected_rows=select_rows,
                        page_action='native',
                        page_current= 0,
                        page_size= 10,
                        style_header={
                            'backgroundColor': 'rgb(23, 45, 101)',
                            'color': 'white',
                            'fontWeight': 'bold'
                        },

                        style_table={
                            'height': 500,
                        },
                        style_cell={
                            'font-family': 'HSE Font',
                            'minWidth': 200,
                            'width': 200,
                            'maxWidth': 200,
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                        },
                        style_data={
                            'whiteSpace': 'normal',
                            'height': 'auto',
                        }
                    )