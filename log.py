log_data = [
    ("2023-10-26 10:00:00", "INFO", "User logged in"),
    ("2023-10-26 10:01:00", "ERROR", "Database connection failed"),
    ("2023-10-26 10:01:30", "INFO", "Data processed successfully"),
    ("2023-10-26 10:02:00", "WARN", "Low disk space"),
    ("2023-10-26 10:03:00", "ERROR", "Database connection failed"),
    ("2023-10-26 10:04:00", "INFO", "User logged out"),
    ("2023-10-26 10:05:00", "ERROR", "Null pointer exception"),
    ("2023-10-26 10:05:30", "DEBUG", "Debugging user session"),
]

error_logs = [log for log in log_data if log[1] == "ERROR"]

print("ERROR Logs:")
for log in error_logs:
    print(log)

db_error_count = sum(
    1 for log in error_logs if log[2] == "Database connection failed"
)

print("\nDatabase connection failed count:", db_error_count)

first_warn = next((log for log in log_data if log[1] == "WARN"), None)

if first_warn:
    print("\nFirst WARN Log:")
    print("Timestamp:", first_warn[0])
    print("Message:", first_warn[2])
else:
    print("\nNo WARN log found")

sorted_logs = sorted(log_data, key=lambda x: x[0])

print("\nSorted Logs:")
for log in sorted_logs:
    print(log)
all_short = all(len(log[2]) < 100 for log in log_data)
has_critical = any(log[1] == "CRITICAL" for log in log_data)

print("\nAll messages shorter than 100 chars:", all_short)
print("Any CRITICAL logs:", has_critical)

new_log = ("2023-10-26 10:06:00", "INFO", "System check complete")

log_data.append(new_log)

print("\nUpdated Log Data:")
for log in log_data:
    print(log)