def validate_inputs(num_working_days, num_ot_hours, num_late_days):
  if isinstance(num_working_days, str):
    return "Working days must be an integer"
  if isinstance(num_ot_hours, str):
    return "Total OT hours must be an integer"
  if isinstance(num_late_days, str):
    return "Late days must be an integer"

  if num_working_days < 0:
    return "Working days must be a positive number"
  if num_ot_hours < 0:
    return "Total OT hours must be a positive number"
  if num_late_days < 0:
    return "Late days must be a positive number"
  
  if num_working_days == 0 and (num_ot_hours or num_late_days):
    return "Invalid Inputs"
  elif num_working_days > 31:
    return "Invalid Working Days"
  elif num_late_days > num_working_days:
    return "Late days must be less than Working Days"

format_outout = lambda salary: f'{salary:,}'

def calculate_salary(num_working_days, num_ot_hours, num_late_days):
  DAILY_PAYMENT = 340
  OT_PAYMENT = 60

  validate_inputs_result = validate_inputs(num_working_days, num_ot_hours, num_late_days)

  if type(validate_inputs_result) != str:
    MONTH_PAYMENT = DAILY_PAYMENT * num_working_days
    TOTAL_OT_PAYMENT = OT_PAYMENT * num_ot_hours

    if num_late_days == 0 and num_working_days != num_late_days:
      if num_ot_hours > num_working_days * 3:
        ot_payment_result = (num_working_days * 3) * OT_PAYMENT
        return format_outout(MONTH_PAYMENT + ot_payment_result)
      else:
        return format_outout(MONTH_PAYMENT + TOTAL_OT_PAYMENT + 1000)
    else:
      if num_working_days == num_late_days:
        return 0
      return format_outout(MONTH_PAYMENT + TOTAL_OT_PAYMENT)
  else:
    return validate_inputs_result
