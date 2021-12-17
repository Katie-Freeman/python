with open("emails.txt") as file:
    emails = file.read()

duplicate_emails = emails.split(", ")
duplicate_free_emails = []

for email in duplicate_emails:
    if email not in duplicate_free_emails:
        duplicate_free_emails.append(email)
#option 1
#with open("duplicate_free_emails.txt", "w") as file:
 #   for email in duplicate_free_emails:
  #      file.write(email)
   #     file.write(",")
#option 3
content = ",".join(duplicate_free_emails)
with open("duplicate_free_emails.txt", "w") as file:
    file.write(content)
    file.write("/n")
    