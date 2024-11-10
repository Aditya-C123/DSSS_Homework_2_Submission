import unittest
from math_quiz import random_integer, random_operator, mathematical_operation

class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        """
        Test if random numbers generated are within the specified range
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        """
        Test if the random operator is one of the expected operators
        """
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_operator = random_operator()
            self.assertIn(rand_operator, operators)

    def test_mathematical_operation(self):
        """
        Test the mathematical operation function
        """
        test_cases = [
                (5, 2, '+', '5 + 2', 7),(8, 3, '-', '8 - 3', 5),(4, 6, '*', '4 * 6', 24)
            ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
          with self.subTest(num1=num1, num2=num2, operator=operator):
            problem, answer = mathematical_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
