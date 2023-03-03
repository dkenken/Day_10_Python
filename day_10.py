# Exercises #DAy #10

# AGENDA: Functions With Outputs

# def my_fuction():
#     return 3 * 2

# output = my_fuction()
# print(output)


# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"{formated_f_name} {formated_l_name}"

# formated_string = format_name("KenDerLY", "delinoIS")
# print(formated_string)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):

    if month > 12 or month < 1:
      return "Invalid Input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
        
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Calculator program

from art import logo


def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
   return n1 * n2
def divide(n1, n2):
   return n1 / n2  

operations = {
   "+": add,
   "-": substract,
   "*": multiply,
   "/": divide
}

def calculator ():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()