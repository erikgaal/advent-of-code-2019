from unittest import TestCase

from day2.program import run


class TestProgram(TestCase):
    def test_run(self):
        self.assertEqual([2, 0, 0, 0, 99], run([1, 0, 0, 0, 99]))
        self.assertEqual([2, 3, 0, 6, 99], run([2, 3, 0, 3, 99]))
        self.assertEqual([2, 4, 4, 5, 99, 9801], run([2, 4, 4, 5, 99, 0]))
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], run([1, 1, 1, 4, 99, 5, 6, 0, 99]))
