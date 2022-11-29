from typing import List


def filter_query(param: str, data: List[str]) -> List[str]:
    """Search (filter) in data"""
    return list(filter(lambda row: param in row, data))


def map_query(param:str, data: List[str]) -> List[str]:
    col_number = int(param)
    return list(filter(lambda row: row.split(' ')[col_number], data))


def unique_query(data: List[str], *args, **kwargs) -> List[str]:
    result = []
    seen = set()
    for row in data:
        if row in seen:
            continue
        else:
            result.append(row)
            seen.add(row)
    return result


def sort_query(param, data: List[str]) -> List[str]:
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: List[str]) -> List[str]:
    limit = int(param)
    return data[:limit]


CMD_TO_FUNCTION = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
}


def build_query(cmd, param, filename, data=None):
    if not data:
        with open(f'data/{filename}') as file:
            data = list(map(lambda row: row.strip(), file))
    return CMD_TO_FUNCTION[cmd](param=param, data=data)
