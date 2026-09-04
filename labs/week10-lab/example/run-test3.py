print("\n=== STRING METHODS ===")
text = input("Enter your text to change capitalize : ")

# Case methods
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")

# Search methods
print(f"Find 'world': {text.find('world')}")
print(f"Count 'o': {text.count('o')}")
print(f"Starts with 'welcome': {text.startswith('welcome')}")
print(f"Ends with 'python': {text.endswith('python')}")

# Modification methods
print(f"Replace 'python' with 'java': {text.replace('python', 'java')}")
words = text.split()
print(f"Split into words: {words}") # Split into words: ['welcome', 'world', 'class']
print(f"Join with '-': {'-'.join(words)}")

# Validation methods
test_str = "Hello123"
print(f"\nValidation methods for '{test_str}':")
print(f"isalnum(): {test_str.isalnum()}")
print(f"isalpha(): {test_str.isalpha()}")
print(f"isdigit(): {test_str.isdigit()}")
print(f"isupper(): {test_str.isupper()}")
print(f"islower(): {test_str.islower()}")