# 1. Create an empty list to keep track of unique emails (to avoid duplicates)
seen_emails = []

print("Starting the data cleaning process...")


with open("dirty_data.txt", "r") as dirty_file, open("clean_data.txt", "w") as clean_file:
    
    
    for line in dirty_file:

        name, email = line.split(",")
        
        clean_name = name.strip().capitalize()
        
        clean_email = email.strip().lower()


        if clean_email not in seen_emails:

            seen_emails.append(clean_email)
        
            clean_file.write(f"{clean_name},{clean_email}\n")

print("Data cleaning complete! Check your folder for 'clean_data.txt'.")