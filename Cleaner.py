# 1. Create an empty list to keep track of unique emails (to avoid duplicates)
seen_emails = []

print("Starting the data cleaning process...")

# 2. Open the dirty file to read ('r') and a new file to write the clean data ('w')
with open("dirty_data.txt", "r") as dirty_file, open("clean_data.txt", "w") as clean_file:
    
    # 3. Loop through each line in the messy file
    for line in dirty_file:
        
        # Split the line into Name and Email using the comma
        name, email = line.split(",")
        
        # Clean up the Name: remove spaces and fix capitalization (e.g., " jOhN " -> "John")
        clean_name = name.strip().capitalize()
        
        # Clean up the Email: remove spaces and make it all lowercase
        clean_email = email.strip().lower()
        
        # 4. Check for duplicates: Only save if we haven't seen this email before
        if clean_email not in seen_emails:
            # Add it to our tracker list
            seen_emails.append(clean_email)
            
            # Write the beautifully cleaned data into our new file
            clean_file.write(f"{clean_name},{clean_email}\n")

print("Data cleaning complete! Check your folder for 'clean_data.txt'.")