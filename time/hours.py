# converting hours
time_in_hours = float(input("enter a number in hours: "))
seconds_to_hours = time_in_hours * (60 * 60)
minute_to_hours = time_in_hours * (60 * 60)
hours_to_hours = time_in_hours
days_to_hours = time_in_hours / 24
print(f"your time in days is {days_to_hours} days", f" \nyour time in hours is {hours_to_hours} hours",
      f"\nyour time in minutes is {minute_to_hours} min", f"\nyour time in seconds is {seconds_to_hours} sec")
