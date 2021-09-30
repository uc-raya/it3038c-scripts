def calculate():
    operation = input('''
Select the math operation you would like to use:
+ for addition
- for subtraction
/ for division
* for multiplication
''')

    number_1 = int(input('Enter the first number: '))
    number_2 = int(input('Enter the first number: '))

#Addition
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

#Subtraction
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

#Division
    elif operation == '/':
          print('{} / {} = '.format(number_1, number_2))
          print(number_1 / number_2)

#Multiplication
    elif operation == '*':
          print('{} * {} = '.format(number_1, number_2))
          print(number_1 * number_2)

    else:
          print('You entered an operation we cannot do. Sorry, try again!')

    
    again()

def again():
    calc_again = input('''
    Do you want to do another operation?
    Y or N?
    ''')

    if calc_again.upper() == 'Y':
            calculate()
    elif calc_again.upper() == 'N':
            print('Okay. Goodbye!')
    else:
            again()

calculate()