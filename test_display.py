from function_calculate_salary import calculate_salary
import pytest

@pytest.mark.parametrize(
	"num_working_days, num_ot_hours, num_late_days, expected_result", [
	(20,20,20,0),
])

def test_display_salary(num_working_days, num_ot_hours, num_late_days, expected_result):
	actual_result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
	assert actual_result == expected_result