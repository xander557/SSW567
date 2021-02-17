"""
    author: xander
    This file takes three input as sides of a triangle and tells us what
    kind of triangle it is.


"""

import unittest


def classify_triangle(a, b, c):
    result = []
    # exclude edge cases
    if not a or not b or not c:
        return result
    if type(a) == str or type(b) == str or type(c) == str:
        return result
    if a <= 0 or b <= 0 or c <= 0:
        return result
    # if a + b <= c or a + c <= b or b + c <= a:
    #     return result

    # classification
    if a == b and b == c:
        result.append("equilateral")
    if a == b or b == c:
        result.append("isosceles")
    if a != b and b != c:
        result.append("scalene")
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        result.append("right")
    return result


# Test case for the triangle
class Test(unittest.TestCase):
    def test_count_vowels(self):
        # functional case
        self.assertEqual(classify_triangle(2, 2, 2), ['equilateral', 'isosceles'])
        self.assertEqual(classify_triangle(2, 2, 3), ['isosceles'])
        self.assertEqual(classify_triangle(10, 9, 7), ['scalene'])
        self.assertEqual(classify_triangle(3, 4, 5), ['scalene', 'right'])

        # edge case
        self.assertEqual(classify_triangle(0, 4, 5), [])
        self.assertEqual(classify_triangle(-5, 4, 5), [])
        self.assertEqual(classify_triangle(None, None, 1), [])
        self.assertEqual(classify_triangle(2, 1, 1), [])
        self.assertEqual(classify_triangle(3, "three ", 1), [])

# main
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
