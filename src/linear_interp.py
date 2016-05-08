# coding=utf8


def linear_interp(x_s, y_s):
    n = len(x_s)

    def f(x):
        i = 0
        while i < n and x_s[i] < x:
            i += 1

        return y_s[i - 1] + (x - x_s[i - 1]) * (y_s[i] - y_s[i - 1]) / (x_s[i] - x_s[i - 1])
    return f



