from function_calculate_salary import calculate_salary
import pytest

# test case ID: 1
def test_num_working_days_30_num_ot_hours_0_num_late_days_0():
  num_working_days = 30
  num_ot_hours = 0
  num_late_days = 0
  expected_result = "11,200"
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 2
def test_num_working_days_30_num_ot_hours_0_num_late_days_3():
  num_working_days = 30
  num_ot_hours = 0
  num_late_days = 3
  expected_result = "10,200"
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 3
def test_num_working_days_30_num_ot_hours_2_num_late_days_0():
  num_working_days = 30
  num_ot_hours = 2
  num_late_days = 0
  expected_result = "11,320"
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 4
def test_num_working_days_30_num_ot_hours_2_num_late_days_2():
  num_working_days = 30
  num_ot_hours = 2
  num_late_days = 2
  expected_result = "10,320"
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 5
def test_num_working_days_0_num_ot_hours_0_num_late_days_0():
  num_working_days = 0
  num_ot_hours = 0
  num_late_days = 0
  expected_result = 0
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 6
def test_num_working_days_0_num_ot_hours_4_num_late_days_0():
  num_working_days = 0
  num_ot_hours = 4
  num_late_days = 0
  expected_result = "Invalid Inputs"
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 7
def test_num_working_days_32_num_ot_hours_0_num_late_days_0():
  num_working_days = 32
  num_ot_hours = 0
  num_late_days = 0
  expected_result = "Invalid Working Days"
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 8
def test_num_working_days_15_num_ot_hours_60_num_late_days_0():
  num_working_days = 15
  num_ot_hours = 60
  num_late_days = 0
  expected_result = "7,800"
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 9
def test_num_working_days_10_num_ot_hours_0_num_late_days_20():
  num_working_days = 10
  num_ot_hours = 0
  num_late_days = 20
  expected_result = "Late days must be less than Working Days"
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 10
def test_num_working_days_0_num_ot_hours_minus_1_num_late_days_0():
  num_working_days = 0
  num_ot_hours = -1
  num_late_days = 0
  expected_result = "Total OT hours must be a positive number"
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 11
def test_num_working_days_27_num_ot_hours_0_num_late_days_27():
  num_working_days = 27
  num_ot_hours = 0
  num_late_days = 27
  expected_result = 0
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result

# test case ID: 12
def test_num_working_days_15_num_ot_hours_12_num_late_days_ABC():
  num_working_days = 15
  num_ot_hours = 12
  num_late_days = "ABC"
  expected_result = "Late days must be an integer"
  actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
  assert expected_result == actual_result
