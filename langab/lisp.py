import builtins


def let(**kwargs):
    for k, v in kwargs.items():
        setattr(builtins, k, v)

    return lambda x: x
