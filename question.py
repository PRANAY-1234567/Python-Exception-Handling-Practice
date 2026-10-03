#1) Write a program that accepts two numbers and performs 
#division. Handle ZeroDivisionError if the second number is 0. 

'''a=int(input("Enter the number:"))
b=int(input("Enter the number: "))

try:
    print(a/b)
except ZeroDivisionError :
    print('Error Done')'''

#2) Ask the user to enter an integer. Handle ValueError if the user enters text instead of a number. 

'''try:
    a = int(input("Enter the integer: "))
    print("You enter the integer: ", a)
except ValueError:
    print("Error Handling")'''

#3) numbers = [10, 20, 30, 40, 50]
#Ask the user for an index and print the value. Handle IndexError.

numbers = [10, 20, 30, 40, 50]

'''try:
    print(numbers[6])
except IndexError:
    print("Index Error Handling")'''

#4.student = {"name": "Rahul", "age": 22, "course": "Python"}
#Ask the user for a key and print its value. Handle KeyError.
'''
student = {"name": "Rahul", "age": 22, "course": "Python"}
try:
    key = input("Enter a key: ")
    print("Value:", student[key])

except KeyError:
    print("Error: Key does not exist.")'''

#5.Write a program that accepts two inputs and performs division. Handle both ValueError and ZeroDivisionError. 
'''
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ValueError:
    print("Error: Please enter numbers only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")'''

#6.Write a program that converts "abc" into an integer.and display the exception message.
'''try:
    num = int("abc")
    print(num)

except ValueError as e:
    print("Exception:", e)'''

#7.Write a program to open data.txt and read its contents. Handle FileNotFoundError.Use finally to display:
#File operation completed
'''try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: data.txt file not found.")

finally:
    print("File operation completed")'''


# 8.Create a login program.
# username = "admin"
# password = "python123"
# Ask the user for username and password.Handle invalid input and use finally to print:
# Login process completed
'''username = "admin"
password = "python123"

try:
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == username and pwd == password:
        print("Login successful")
    else:
        print("Invalid username or password")

except ValueError:
    print("Invalid input")

finally:
    print("Login process completed")'''


#9.Create a situation where an undefined variable is accessed. Handle NameError. 
try:
    a=a+15
except NameError:
    print("Name Error Handling")


