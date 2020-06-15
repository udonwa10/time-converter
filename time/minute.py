# converting minutes
time_in_minute = float(input("please enter your time here in minutes: "))
seconds_to_minutes = time_in_minute * (60)
hours_to_minutes = time_in_minute / (60)
days_to_minutes = time_in_minute / (24 * 60)
minute_to_minutes = time_in_minute
print(f"your time in days is {days_to_minutes} days", f" \nyour time in hours is {hours_to_minutes} hours",
      f"\nyour time in minutes is {minute_to_minutes} min", f"\nyour time in seconds is {seconds_to_minutes} sec")
