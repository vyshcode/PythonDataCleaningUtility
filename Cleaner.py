print("Starting the data cleaning process...")

# 1. Using a set for O(1) lightning-fast duplicate lookups
seen_emails = set()
invalid_lines_count = 0

# 2. Open both files cleanly using a single 'with' block
with open("dirty_data.txt", "r") as dirty_file, open("clean_data.txt", "w") as clean_file:
    for line_num, line in enumerate(dirty_file, 1):
        # 3. Strip surrounding whitespace first
        line = line.strip()
        if not line:
            continue  # Skip empty lines entirely

        # 4. Error Handling: Ensure the line actually splits into exactly two parts
        try:
            name, email = line.split(",", 1)  # Maxsplit=1 handles names with commas safely
        except ValueError:
            print(f" Skipping malformed data on line {line_num}: '{line}'")
            invalid_lines_count += 1
            continue

        # 5. Smarter string normalization
        clean_name = name.strip().title()  # .title() turns "john doe" into "John Doe"
        clean_email = email.strip().lower()

        # 6. Set lookup and writing
        if clean_email not in seen_emails:
            seen_emails.add(clean_email)
            clean_file.write(f"{clean_name},{clean_email}\n")

# 7. Informative feedback summary
print("\n--- Data Cleaning Complete! ---")
print(f" Successfully processed and saved to 'clean_data.txt'")
print(f" Unique records kept: {len(seen_emails)}")
if invalid_lines_count > 0:
    print(f" Skipped lines (corrupted data): {invalid_lines_count}")