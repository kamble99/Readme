import re

# Sample string
text = "Hello, my email is test123@gmail.com and phone number is 9876543210."

print("Original Text:")
print(text)

# ---------------- STRING OPERATIONS ---------------- #

# Convert to lowercase
print("\nLowercase:")
print(text.lower())

# Convert to uppercase
print("\nUppercase:")
print(text.upper())

# Replace word
print("\nReplace 'Hello' with 'Hi':")
print(text.replace("Hello", "Hi"))

# Split string
print("\nSplit string:")
print(text.split(" "))

# Check substring
print("\nCheck if 'email' exists:")
print("email" in text)

# ---------------- REGEX OPERATIONS ---------------- #

# Find email
email = re.findall(r'\S+@\S+', text)
print("\nExtracted Email:")
print(email)

# Find phone number (10 digits)
phone = re.findall(r'\d{10}', text)
print("\nExtracted Phone Number:")
print(phone)

# Find all digits
digits = re.findall(r'\d', text)
print("\nAll Digits:")
print(digits)

# Replace digits with '*'
masked = re.sub(r'\d', '*', text)
print("\nMasked Text:")
print(masked)

# Check pattern
match = re.search(r'email', text)
if match:
    print("\nPattern 'email' found")
else:
    print("\nPattern not found")

# Split using regex
split_text = re.split(r'\s', text)
print("\nSplit using regex:")
print(split_text)