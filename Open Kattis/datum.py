month_lengths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

days = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]

D, M = [int(num) for num in input().split()]

print(days[(sum(month_lengths[: M]) + D) % 7])
