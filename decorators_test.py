def decorators(func):
    def wrapper():
        print("do_something")
        func()
    return wrapper
@decorators
def test_hi():
    print("hi")

test_hi()

# example of args in decorator

def convert_negatives_to_positive(func):
    def wrapper(*args, **kwargs):
        # Convert negative values to positive
        args = [abs(arg) if arg < 0 else arg for arg in args]
        kwargs = {key: abs(value) if value < 0 else value for key, value in kwargs.items()}
        # Call the original function with modified arguments
        return func(*args, **kwargs)
    return wrapper

# Example usage:
@convert_negatives_to_positive
def my_sum(*args):
    return sum(args)

# Test the decorated function
result = my_sum(1, -2, 3, -4)
print(result)  # Output will be 10 (1 + 2 + 3 + 4)



# class based decorator

class StatefulDecorator:
    def __init__(self, func):
        self.func= func
        self.state=0
    def __call__(self, *args, **kwargs):
        self.state+=1
        return self.func(*args, **kwargs)


@StatefulDecorator
def  my_function():
    print("inside the function")


my_function()
my_function()
