import jmespath


def sort_by_key(
    data: list[dict], key_list: list[str], reverse: bool = False
) -> list[dict]:
    key_list.reverse()
    expr = ""
    for key in key_list:
        if not expr:
            expr = f"sort_by(@, &{key})"
        else:
            expr = f"sort_by({expr}, &{key})"

        if reverse:
            expr = f"{expr}.reverse(@)"

    return jmespath.search(expression=expr, data=data)
