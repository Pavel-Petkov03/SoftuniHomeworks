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
        result = self.student.add_notes('a', [30, 31, 32])
        self.assertEqual(result, "Notes have been updated")
        self.assertDictEqual({'a': [1, 2, 3, [30, 31, 32]], 'b': [3, 4, 5], 'c': [6, 7, 8]}, self.student.courses)
        self.assertListEqual([1, 2, 3, [30, 31, 32]], self.student.courses['a'])

    def test_add_notes_with_not_existing_course__expected_error(self):
        with self.assertRaises(Exception)as ex:
            self.student.add_notes('z', [1, 2])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_and_course_in_courses_expected_remove(self):
        result = self.student.leave_course('a')
        self.assertEqual(result, 'Course has been removed')
        self.assertDictEqual({'b': [3, 4, 5], 'c': [6, 7, 8]}, self.student.courses)
        self.assertTrue('a' not in self.student.courses)

    def test_leave_course_and_course_not_in_courses_expected__exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('d')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()


