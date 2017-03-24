def golden_ratio(func, start, end, length):
    #Precalulated ratio
    ratio = 0.382
    l = end - start
    while abs(l) > length:
        x1 = start + ratio * l
        x2 = start + (1 - ratio) * l
        if func(x1) > func(x2):
            start = x1
        else:
            end = x2
        l = end - start
    return [start, end]

