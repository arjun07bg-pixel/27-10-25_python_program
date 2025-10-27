'''
# Question - 1
a = int(input("Enter a value="))
b = int(input("Enter b value="))
c = int(input("Enter c value="))

if a > b and a > c:
    print("a")
elif b > a and b > c:
    print("b")
else:
    print("c")   

# Question - 2
n = int(input("Enter n value="))
l = int(input("Enter l value="))
r = int(input("Enter r value="))

if n > l and n < r:
    print("Yes")
else:
    print("No")    

    
# Question - 3

number1 = int(input("Enter the number1="))
number2 = int(input("Enter the number2="))
operator = input("Enter operator (+,-,*,/): ")

match operator:
    case '+':
        print(number1 + number2)
    case '-':
        print(number1 - number2)
    case '*':
        print(number1 * number2)
    case '/':
        print(number1 / number2)
    case _:
        print("Invalid operator")  '''


