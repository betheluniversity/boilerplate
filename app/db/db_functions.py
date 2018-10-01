from app.db.oracle import conn


def get_results(result, label=""):
    ret = {}
    for i, row in enumerate(result):
        row_dict = {}
        for item in row:
            if isinstance(item, str) or isinstance(item, unicode):
                item = item.split(":", 1)
            else:
                # blob
                item = item.read()
            if len(item) > 1:
                row_dict[item[0]] = item[1]
            else:
                # if the result set doens't have key / value pairs
                # use a custom label
                row_dict[label] = item[0]

        ret[int(i)] = row_dict

    return ret


def example_call(username):
    try:
        call_cursor_bw = conn.cursor()
        result_cursor_bw = conn.cursor()
        call_cursor_bw.callproc('made_up.process_name', (username, result_cursor_bw,))
        r = result_cursor_bw.fetchall()
        return get_results(r)
    except:
        return {}
