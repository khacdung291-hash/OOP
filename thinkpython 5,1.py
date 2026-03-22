import time
seconds = time.time()
days = int(seconds // 86400)
remaining_seconds = seconds % 86400
hours = int(remaining_seconds // 3600)
remaining_seconds %= 3600
minutes = int(remaining_seconds // 60)
seconds = int(remaining_seconds % 60)
print("Days since epoch:", days)
print("Current time:", hours, ":", minutes, ":", seconds)