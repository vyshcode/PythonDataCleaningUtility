print("Starting the data cleaning process...")

# Track uniques and bad rows
seen_emails = set()
invalid_lines_count = 0

with open("dirty_data.txt", "r") as dirty_file, open("clean_data.txt", "w") as clean_file:
    for line_num, line in enumerate(dirty_file, 1):
        line = line.strip()
        if not line:
            continue  

        # maxsplit=1 prevents breaking if a name contains a comma
        try:
            name, email = line.split(",", 1)  
        except ValueError:
            print(f"Skipping malformed data on line {line_num}: '{line}'")
            invalid_lines_count += 1
            continue

        # Standardize formatting
        clean_name = name.strip().title()  
        clean_email = email.strip().lower()

        # Deduplicate based on email
        if clean_email not in seen_emails:
            seen_emails.add(clean_email)
            clean_file.write(f"{clean_name},{clean_email}\n")

print("\nFinished cleaning.")
print(f"Saved to clean_data.txt ({len(seen_emails)} unique records)")
if invalid_lines_count > 0:
    print(f"Skipped {invalid_lines_count} broken lines.")