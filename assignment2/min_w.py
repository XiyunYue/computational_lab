def wmin(b_k):
    click_max = 0
    click_sum = 0
    for i in b_k:
        if i != 0:
            click_sum += 1
            if click_sum > click_max:
                click_max = click_sum
        else:
            click_sum = 0
    w_mini = click_max * 2 + 1
    return w_mini