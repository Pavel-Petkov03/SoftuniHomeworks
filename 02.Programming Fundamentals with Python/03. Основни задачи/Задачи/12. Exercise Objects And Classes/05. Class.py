# Create a class Class. The __init__ method should receive the name of the class. It should also have 2 lists
# (students and grades). Create a class attribute __students_count equal to 22.
# The class should also have 3 additional methods:
# •	add_student(name, grade) - if there is space in the class, add the student and the grade in the two lists
# •	get_average_grade() - returns the average of all existing grades formatted to the second decimal point
# (as a number)
# •	__repr__ - returns the string (single line): "The students in {class_name}: {students}. Average grade: "{get_average_grade()}". The students must be seperated by ", "

class Class:
	__students_count = 22

	def __init__(self, name):
		self.name = name
		self.students = []
		self.grades = []

	def add_student(self, name, grade):
		if Class.__students_count:
			Class.__students_count -= 1
			self.students.append(name)
			self.grades.append(float(grade))

	def get_average_grade(self):
		return sum(self.grades) / len(self.students)

	def __repr__(self):
		score = self.get_average_grade()
		return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {score:.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
