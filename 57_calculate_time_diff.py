# Calculate the difference between two times
from datetime import datetime

time1 = datetime(2023, 1, 1, 12, 0, 0)
time2 = datetime(2023, 1, 2, 14, 30, 0)

difference = time2 - time1
print("Time 1:", time1)
print("Time 2:", time2)
print("Difference:", difference)
