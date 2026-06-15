#name = input("What is your name? ")
#country = input("Where are you from? ")
#things = input("What are your favourite things? ")
#print("hello, my name is " + name + ".\nI am from " + country + ".\nMy favourite things are " + things + ".\n")


#a = int(input("Number A: "))
#b = int(input("Number B: "))
#print("A + B = ", a + b)
#print("A - B = ", a - b)
#print("A * B = ", a * b)
#if b == 0:
#    print("You can not devide by zero")
#else:
#    print("A / B", a / b)


#number = int(input("Enter a number: "))
#if number %2 == 0:
#    print("It is an even number.")
#else:
#    print("It is an odd number.")

#if number > 0:
#    print("Number is positive.")
#elif number == 0:
#    print("Number is a 0.")
#else:
#     print("Number is negative.")


# correct_login = "Nikodem"
# correct_password = "test"
# login = input("Type in your login: ")
# while login != correct_login:
#     print("Incorrect login. Try again.")
#     login = input("Type in your login: ")
# password = input("Type in your password: ")
# while password != correct_password:
#     print("Incorrect password. Try Again.")
#     password = input("Type in your password: ")
# print("Successfully logged in!")


# age = int(input("How old are you? "))
# if age >= 16:
#     payment = input("Did you pay? (Yes/No) ")
#     if payment == "Yes":
#         score = int(input("What is your score? (0-100) "))
#         if score >= 80:
#             print("High level access granted.")
#         elif score < 80 and score > 50:
#             print("Intermediate level access granted.")
#         else:
#             print("Access denied.")
#     else:
#         print("Access denied.")
# else:
#     print("Access denied.")


# for i in range(1, 5):
#     print("*"*i)


# balance = 1000
# def CheckBalance():
#     print("Balance: ", balance)
# def DepositMoney():
#     global balance
#     deposit = int(input("How much money would you like to deposit? "))
#     balance += deposit
#     print("Balance is now ", balance)
# def WithdrawMoney():
#     global balance
#     withdraw = int(input("How much money would you like to withdraw? "))
#     while withdraw > balance:
#         print("Error! Balance can't be negative.")
#         withdraw = int(input("How much money would you like to withdraw? "))
#     balance -= withdraw
#     print("Balance is now ", balance)
# def error():
#     print("Error! Try again.")

# temp = 0
# while temp != 4:
#     choice = int(input("Hello! (1 - check balance, 2 - deposit money, 3 - withdraw money, 4 - exit) "))
#     match choice:
#         case 1:
#             CheckBalance()
#         case 2:
#             DepositMoney()
#         case 3:
#             WithdrawMoney()
#         case 4:
#             temp = 4
#         case _:
#             error()


# fruits = ["mango", "orange", "apple", "banana", "pear"]
# print(fruits[0], fruits[4])
# fruits.insert(1, "cherry")
# fruits[3] = "strawberry"
# fruits.pop()
# print(fruits)


students_number = int(input("How many students? "))
students = []
grades = []
i = 0
while i < students_number:
    students.append(input(f"What's the name of the student number {i + 1}? "))
    grades.append(int(input(f"What is {students[i]}'s grade? (0-100) ")))
    i += 1
status = 0
while status != 5:
    status = int(input("What action would you like to do? (1 - show students, 2 - check, 3 - classification, 4 - statistics, 5 - exit) "))
    if status == 1:
        print(f"List of students: {students}")
    elif status == 2:
        name = input("What student's grade would you like to check? ")
        if name in students:
            student_id = students.index(name)
            if grades[student_id] <= 50:
                print(f"{name} failed.")
            elif grades[student_id] > 50 and grades[student_id] < 70:
                print(f"{name} has a grade of average.")
            elif grades[student_id] >= 70 and grades[student_id] < 90:
                print(f"{name} has a good grade.")
            elif grades [student_id] >= 90:
                print(f"Excellent {name}!")
        else:
            print("Student doesn't exist.")
    elif status == 3:
        classification = list(zip(grades, students))
        classification.sort(reverse=True)
        print(classification)
    elif status == 4:
        print(f"Number of students: {len(students)}")
        grades_sum = 0
        for i in range(len(grades)):
            grades_sum += grades[i]
        average = grades_sum / len(grades)
        print(f"Average grade is {average}.")
        excellent = 0
        fail = 0
        for i in range(len(students)):
            if grades[i] >= 90:
                excellent += 1
            elif grades[i] <= 50:
                fail += 1
        print(f"There is {excellent} excellent grades and {fail} people failed.")


    
    