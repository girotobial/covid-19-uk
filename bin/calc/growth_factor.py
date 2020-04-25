# growth_ratio.py

from .divide import divide

def growth_ratio(iterable):
    growth_list = []
    for i, val in enumerate(iterable):
        if i == 0:
            ratio = 1

        if i > 0:
            ratio = divide(val, iterable[i - 1], 1)

        growth_list.append(ratio)
    return growth_list