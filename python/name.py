defaults = {
    'a': 1,
    'b': 2
}


def f(x, **kwa):
    # Each time the function is called, merge the default values and the provided arguments
    # For python >= 3.5:
    args = {**defaults, **kwa}
    # For python < 3.5:
    # Each time the function is called, copy the default values
    args = defaults.copy()
    # Merge the provided arguments into the copied default values
    args.update(kwa)
    print(args)

f(1, f=2)

