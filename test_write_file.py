from functions.write_file import write_file

# Test 1: Overwriting existing file
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

# Test 2: Writing to a new sub-directory (Tests your os.makedirs logic!)
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

# Test 3: Security check (Should fail)
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))