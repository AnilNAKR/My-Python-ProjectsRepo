def add(*args):
    sum_output = 0
    for n in args:
        sum_output += n
    print(sum_output)


add(3, 4, 5)


def calculate(**kwargs):
    print(kwargs)


calculate(a=2, b=3, c=4)


class Car:
    def __init__(self, **kw):
        self.build = kw.get("build")
        self.model = kw.get("model")
#         self.build = kw["build]
# The above line return 'error' if there is argument is not passed
# And kw.get("build) will return None if argument is not passed


cars = Car(build = "Nissan", model = "GTR")
print(cars.model)
