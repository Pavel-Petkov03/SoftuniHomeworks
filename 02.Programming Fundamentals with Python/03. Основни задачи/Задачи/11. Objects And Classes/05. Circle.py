# Create a class Circle. In the __init__
# method the circle should only receive one parameter (its diameter). Create a class attribute called __pi that is
# equal to 3.14. The class should also have the following methods:
# 	calculate_circumference() - returns the circumference of the circle
# 	calculate_area() - returns the area of the circle
# 	calculate_area_of_sector(angle) - given the central angle in degrees, returns the area that fills the sector
class Circle:
	def __init__(self, diameter):
		self.diameter = diameter
		self.radius = diameter / 2
		self.pi = 3.14

	def calculate_circumference(self):
		return self.pi * self.diameter

	def calculate_area(self):
		return self.pi * self.radius**2

	def calculate_area_of_sector(self, angle):
		return (angle / 360) * self.pi * self.radius**2

circle = Circle(10)
angle_ = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle_):.2f}")
