days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

count = 0
for day in days_of_week:
    count += day.count("e")

print(count)
