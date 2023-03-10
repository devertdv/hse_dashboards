def select_rows_big_table(df, click_data):

    select_rows = []
    if click_data is not None and "entry" in click_data["points"][0] and click_data["points"][0]["entry"] != click_data["points"][0]["label"]:
        keyword = click_data["points"][0]["label"]
        for idx, row in df.iterrows():
            cell = row["Author Keywords"].split("; ")
            if keyword in cell:
                select_rows.append(idx)
    else:
        select_rows = [i for i in range(df.shape[0])]

    return select_rows
