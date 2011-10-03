


def chop(val, sorted_list):
    if sorted_list:
        m = len(sorted_list) / 2
        head = sorted_list[:m]
        tail = sorted_list[m+1:]
        if val == sorted_list[m]:
            return m
        elif val < sorted_list[m]:
            return chop(val, head)
        else:
            return len(head) + chop(val, tail)
    else:
        return -1
