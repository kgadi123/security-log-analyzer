from collections import defaultdict

log_file = "sample_log.txt"

failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        if "Failed login" in line:
            parts = line.split()
            ip = parts[-1]
            failed_attempts[ip] += 1

print("=== Security Log Analysis ===\n")

for ip, count in failed_attempts.items():
    print(f"IP Address: {ip} | Failed Attempts: {count}")

    if count >= 3:
        print("⚠ ALERT: Possible brute-force attack!\n")