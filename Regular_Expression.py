import re

text = "Hello, my email addresses are user1@example.com and user2@example.org."

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

email_addresses = re.findall(pattern, text)

first_email = re.search(pattern, text)

print("All email addresses found:", email_addresses)
if first_email:
    print("First email address found:", first_email.group())
else:
    print("No email address found.")
