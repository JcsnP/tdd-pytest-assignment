from function_calculate_salary import calculate_salary

try:
	num_working_days = int(input("Working days: "))
	num_ot_hours = int(input("Total OT hours: "))
	num_late_days = int(input("Late days: "))

	result = calculate_salary(num_working_days, num_ot_hours, num_late_days)
	print(f'salary = {result}')
except ValueError:
	print('Please input only integer.')