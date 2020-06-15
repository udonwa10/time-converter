# converting seconds
time = float(input("Enter time in seconds: "))
hours = time / (3600)
days = time / (24 * 60 * 60)
seconds = time
minutes = time / (60)
print(f"your time in days is {days} days", f" \nyour time in hours is {hours} hours",
      f"\nyour time in minutes is {minutes} min", f"\nyour time in seconds is {seconds} sec")
