# Create a class called Flower. Upon initialization, the class should receive name
# and water_requirements. The flower should also have an attribute called is_happy
# (False by default) and a method called water(quantity), which will water the flower.
# If the water is greater than or equal of the requirements of the flower, it becomes happy.
# (set is_happy to True). The last method should be called status() and it should return
# "{name} is happy" if the flower is happy, otherwise it should return "{name} is not happy".
# Submit only the class in the judge system.


x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
