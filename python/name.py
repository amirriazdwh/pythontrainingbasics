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



object
Main
{
def main(args: Array[String]): Unit = {
def add(x: Int)(y:Int): Int = x + y
def multiply(x: Int)(y:Int) = x * y


val
add10multiply10compose = add(10)
_
andThen
multiply(10)
println(add10multiply10compose(5))
println("Goodbye, World!")
}
}

