#searching for a function minimum interval with swenn algorithm


def swenn(func, x0, step):
    step_sign = swenn_get_step_sign(func, x0, step)
    if step_sign is None:
        print('Bad function')
        return
    elif step_sign == 0:
        return [x0-step, x0+step]
    x_k = []
    f_x_k = []
    i = 0
    while i < 10000:
        x0 += (2 ** i) * (step_sign * step)

        if len(x_k) > 0:
            print([x_k[-1], x0])

        if len(x_k) > 0 and f_x_k[-1] < func(x0):
            return [x_k[-1], x0]
        x_k.append(x0)
        f_x_k.append(func(x0))
        i += 1


def swenn_get_step_sign(func, x0, step):
    res = func(x0)
    res_m_delta = func(x0 - step)
    res_p_delta = func(x0 + step)
    print([res_m_delta, res, res_p_delta])
    if res_m_delta >= res >= res_p_delta:
        return 1
    elif res_m_delta <= res <= res_p_delta:
        return -1
    elif res_m_delta >= res <= res_p_delta:
        return 0
    elif res_m_delta <= res >= res_p_delta:
        return None


