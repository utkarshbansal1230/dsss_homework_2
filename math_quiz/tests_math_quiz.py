import unittest
from math_quiz import generate_random_integer, choose_random_operator, create_math_problem

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Random number {rand_num} is out of range!")

    def test_choose_random_operator(self):
        """
        Test if the random operator selected is one of the expected operators: '+', '-', or '*'.
        """
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of selections
            operator = choose_random_operator()
            self.assertIn(operator, valid_operators, f"Unexpected operator selected: {operator}")

    def test_create_math_problem(self):
        """
        Test if math problems are generated correctly with the appropriate answers.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (4, 6, '*', '4 * 6', 24),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Problem {problem} does not match expected {expected_problem}")
            self.assertEqual(answer, expected_answer, f"Answer {answer} does not match expected {expected_answer}")

if __name__ == "__main__":
    unittest.main()
