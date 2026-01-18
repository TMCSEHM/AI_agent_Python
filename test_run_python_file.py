from functions.run_python_file import run_python_file

def run_tests():
    # 1. Successful run: No arguments (Should show usage instructions)
    print("--- Test 1: main.py (No Args) ---")
    print(run_python_file("calculator", "main.py"))
    print("-" * 30)

    # 2. Successful run: With arguments (Should perform calculation)
    print("\n--- Test 2: main.py (With Args: ['3 + 5']) ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("-" * 30)

    # 3. Successful run: Existing test script
    print("\n--- Test 3: tests.py ---")
    print(run_python_file("calculator", "tests.py"))
    print("-" * 30)

    # 4. Security Error: Outside directory
    print("\n--- Test 4: Path Outside Directory (../main.py) ---")
    print(run_python_file("calculator", "../main.py"))
    print("-" * 30)

    # 5. File Error: Nonexistent file
    print("\n--- Test 5: Nonexistent File ---")
    print(run_python_file("calculator", "nonexistent.py"))
    print("-" * 30)

    # 6. Type Error: Not a Python file
    print("\n--- Test 6: Not a Python File (lorem.txt) ---")
    print(run_python_file("calculator", "lorem.txt"))
    print("-" * 30)

if __name__ == "__main__":
    run_tests()