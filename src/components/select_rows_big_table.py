def select_rows_big_table(df, click_data):

    select_rows = []
    if click_data is None or \
        click_data["points"][0]["pointNumber"] == 0 or \
        len(click_data["points"][0]) == 11 and click_data["points"][0]["root"] != click_data["points"][0]["entry"]:

        select_rows = [i for i in range(df.shape[0])]

    else:
        keyword = click_data["points"][0]["label"]
        for idx, row in df.iterrows():
            cell = row["Author Keywords"].split("; ")
            if keyword in cell:
                select_rows.append(idx)

    return select_rows
