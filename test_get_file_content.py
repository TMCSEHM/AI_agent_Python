from functions.get_file_content import get_file_content

# 1. Test Truncation
print("--- Testing Truncation (lorem.txt) ---")
result = get_file_content("calculator", "lorem.txt")
print(f"Length of result: {len(result)}")
print(f"Ends with: {result[-50:]}") # Just print the last bit to see the message
print("\n")

# 2. Test Success cases
print("--- Testing main.py ---")
print(get_file_content("calculator", "main.py"))

print("--- Testing calculator.py ---")
print(get_file_content("calculator", "pkg/calculator.py"))

# 3. Test Security/Error cases
print("--- Testing Outside Directory ---")
print(get_file_content("calculator", "/bin/cat"))

print("--- Testing Non-existent file ---")
print(get_file_content("calculator", "pkg/does_not_exist.py"))