import time
# Question 1
def countdown():
    print("Countdown from 10 to 1:")
    i = 10
    while i > 0:
        print(i)
        time.sleep(1)
        i -= 1
    print("Loop complete!\n")
# Question 2
def even_numbers_range():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    i = start
    print("Even numbers in range:")
    while i <= end:
        if i % 2 == 0:
            print(i, end=" ")
        i += 1
    print("\n")
# Question 3
def sum_of_n():
    n = int(input("Enter a positive number: "))
    i = 1
    total = 0
    print("Summing: ", end="")
    while i <= n:
        total += i
        print(i, end=" + " if i != n else "")
        i += 1
    print(f" = {total}\n")
# Question 4
def input_validation_with_limit():
    attempts = 3
    while attempts > 0:
        num = int(input("Enter a positive number: "))
        if num > 0:
            print("Thank you!\n")
            return
        else:
            print("Invalid. Try again.")
            attempts -= 1
    print("Too many invalid attempts.\n")
# Question 5
def print_characters():
    s = input("Enter a string: ")
    i = 0
    print("Characters in the string:")
    while i < len(s):
        print(s[i])
        i += 1
    print()
# Question 6 
def password_retry():
    correct = "analytics123"
    attempts = 3
    while attempts > 0:
        pwd = input("Enter password: ")
        if pwd == correct:
            print("Access granted.\n")
            return
        else:
            print("Incorrect password.")
            attempts -= 1
    print("Too many failed attempts.\n")
# Question 7
def guess_number():
    secret = 7
    guess = None
    attempts = 0
    print("Guess the number between 1 and 10:")
    while guess != secret:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
    print(f"Correct! You guessed it in {attempts} tries.\n")
# Question 8
def count_digits():
    num = int(input("Enter a positive number: "))
    count = 0
    n = num
    while n > 0:
        n //= 10
        count += 1
    print(f"{num} has {count} digits.")
    print("Even digit count." if count % 2 == 0 else "Odd digit count.\n")
# Queston 9
def multiplication_table():
    num = int(input("Enter number for table: "))
    i = 1
    while i <= 10:
        print(f"{num:2} x {i:2} = {num*i}")
        i += 1
    print()
# Question 10
def average_until_sentinel():
    print("Enter numbers (-1 to stop):")
    total = 0
    count = 0
    num = 0
    while True:
        num = int(input("Enter number: "))
        if num == -1:
            break
        total += num
        count += 1
    if count > 0:
        print(f"Average = {total/count}")
    else:
        print("No numbers entered.\n")

# Main menu
while True:
    print("""
Choose an option:
1. Countdown with Delay
2. Even Numbers in Range
3. Sum of N Numbers with Steps
4. Input Validation (3 attempts)
5. Print Characters of String
6. Password Retry System
7. Guess the Number Game
8. Count Digits with Type
9. Multiplication Table
10. Average Calculator
0. Exit
""")
    choice = input("Enter choice: ")
    if choice == "1":
        countdown()
    elif choice == "2":
        even_numbers_range()
    elif choice == "3":
        sum_of_n()
    elif choice == "4":
        input_validation_with_limit()
    elif choice == "5":
        print_characters()
    elif choice == "6":
        password_retry()
    elif choice == "7":
        guess_number()
    elif choice == "8":
        count_digits()
    elif choice == "9":
        multiplication_table()
    elif choice == "10":
        average_until_sentinel()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")

