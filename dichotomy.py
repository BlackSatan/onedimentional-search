#Reducing size of interval with dichotomy algorithm


def dichotomy(func, start, end, length):
    l = end - start
    while abs(l) > length:
        x_m = (start+end)/2
        x_1 = start + l / 4
        x_2 = end - l / 4
        f_x_1 = func(x_1)
        f_x_m = func(x_m)
        if f_x_1 < f_x_m:
            end = x_m
        elif f_x_1 >= f_x_m:
            f_x_2 = func(x_2)
            if f_x_2 < f_x_m:
                start = x_m
            else:
                start = x_1
                end = x_2
        l = end - start
    return [start, end]
