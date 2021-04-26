import unittest
from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student('pavel', {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [6, 7, 8]})

    def test_init__(self):
        self.assertEqual(self.student.name, 'pavel')
        self.assertEqual(self.student.courses, {'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [6, 7, 8]})
        new_class = Student('a', None)
        self.assertEqual(new_class.courses, {})

    def test_enroll_with_existing_course(self):
        result = self.student.enroll('a', [10, 11, 12], 'none')
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertListEqual(self.student.courses['a'], [1, 2, 3, 10, 11, 12])
        self.assertDictEqual(self.student.courses, {'a': [1, 2, 3, 10, 11, 12], 'b': [3, 4, 5], 'c': [6, 7, 8]})

    def test_enroll_add_course_notes_are_equal_to_Y_ot_empty_str__expected_new_notes(self):
        result = self.student.enroll('d', [11, 12, 13], 'Y')
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertDictEqual({'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [6, 7, 8], 'd': [11, 12, 13]}, self.student.courses)
        self.assertListEqual(self.student.courses['d'], [11, 12, 13])
        new_student = Student('name', {'a': [1]})
        new_student.enroll('b', [1, 2])
        self.assertDictEqual({'a': [1], 'b': [1, 2]}, new_student.courses)

    def test_enroll_new_course_has_been_added_with_empty_notes(self):
        result = self.student.enroll('d', [1, 2, 3], 'testov')
        self.assertEqual(result, 'Course has been added.')
        self.assertDictEqual({'a': [1, 2, 3], 'b': [3, 4, 5], 'c': [6, 7, 8], 'd': []}, self.student.courses)
        self.assertListEqual(self.student.courses['d'], [])

    def test_add_notes_with_existing_course(self):
        pass



        """
        class Student:
            def __init__(self, name: str, courses=None):
                if courses is None:
                    courses = {}
                self.name = name
                self.courses = courses  # {course_name: [notes]}
        
            def enroll(self, course_name: str, notes, add_course_notes: str = ""):
                if course_name in self.courses.keys():
                    [self.courses[course_name].append(x) for x in notes]
                    return "Course already added. Notes have been updated."
        
                if add_course_notes == "Y" or add_course_notes == "":
                    self.courses[course_name] = notes
                    return "Course and course notes have been added."
        
                self.courses[course_name] = []
                return "Course has been added."
        
            def add_notes(self, course_name, notes):
                if course_name in self.courses.keys():
                    self.courses[course_name].append(notes)
                    return "Notes have been updated"
                raise Exception("Cannot add notes. Course not found.")
        
            def leave_course(self, course_name):
                if course_name in self.courses.keys():
                    self.courses.pop(course_name)
                    return "Course has been removed"
                raise Exception("Cannot remove course. Course not found.")
        """
