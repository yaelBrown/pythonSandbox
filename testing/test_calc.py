"""
  Assert Methods: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
"""

import unittest
from unittest.mock import patch
import calc

class TestCalc(unittest.TestCase):
  def setUp(self):
    # runs before every test
    # beforeEach()
    pass

  def tearDown(self):
    # runs after every test
    # afterEach()
    pass

  @classmethod
  def setUpClass(cls):
    # runs before running tests in the class
    # beforeAll()
    pass

  @classmethod
  def tearDownClass(cls):
    # runs after running tests in the class
    # afterAll()
    pass

  # def test_mock_item(self):
  #   # mocking
  #   with patch('employee.requests.get') as mocked_get:
  #     mocked_get.return_value.ok = True
  #     mocked_get.return_value.text = 'Success'

  #     schedule = self.emp_1.monthly_schedule('May')
  #     mocked_get.assert_called_with('http://company.com/Schafer/May')
  #     self.asertEqual(schedule, 'Success')

  def test_add(self):
    result = calc.add(10, 5)
    self.assertEqual(result, 15)

  def test_subtract(self):
    self.assertEqual(calc.subtract(10,5), 5)

  def test_divide(self):
    self.assertRaises(ValueError, calc.divide, 5, 0) # tests is exception is raised


if __name__ == '__main__':
  unittest.main()