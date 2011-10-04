


def recursive_chop(val, sorted_list):
    if sorted_list:
        m = len(sorted_list) / 2
        head = sorted_list[:m]
        tail = sorted_list[m+1:]
        if val == sorted_list[m]:
            return m
        elif val < sorted_list[m]:
            return recursive_chop(val, head)
        else:
            result = recursive_chop(val, tail)
            if result == -1:
                return -1
            else:
                return len(head) + 1 + result
    else:
        return -1

def while_chop(val, sorted_list):
    if sorted_list:
        start, end = 0, len(sorted_list) - 1
        while start <= end:
            m = (start + end) / 2
            if val == sorted_list[m]:
                return m
            elif val < sorted_list[m]:
                end = m - 1
            else:
                start = m + 1
    return -1

def _rec1_chop(val, sorted_list, start, end):
    if start > end:
        return -1
    m = (start + end) / 2
    if val == sorted_list[m]:
        return m
    elif val < sorted_list[m]:
        return _rec1_chop(val, sorted_list, start, m - 1)
    else:
        return _rec1_chop(val, sorted_list, m + 1, end)

def recursive1_chop(val, sorted_list):
    return _rec1_chop(val, sorted_list, 0, len(sorted_list) - 1)
