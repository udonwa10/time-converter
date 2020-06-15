# converting days
time_in_days = float(input("Enter your time in days"))
days_to_days = time_in_days
hours_to_days = time_in_days * (24)
minute_to_days = time_in_days * (24 * 60)
seconds_to_days = time_in_days * (24 * 60 * 60)
print(f"your time in days is {days_to_days} days", f" \nyour time in hours is {hours_to_days} hours",
      f"\nyour time in minutes is {minute_to_days} min", f"\nyour time in seconds is {seconds_to_days} sec")
