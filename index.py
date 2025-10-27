'''
Tara = int(input("Enter the number="))
Jothi = int(input("Enter the number="))
total = Tara + Jothi
if total % 5 == 0:
    print(1)
else:
    print(0)   

N = int(input("Enter the Number="))
if N % 7 == 0:
    print("Yes")
else:
    print("No") 

amount=500
a=int(input("Enter order amount="))
if a <= 500:
    print("extra delivery charge is:50")
    print("total amount:",a+50)
else:
    print("No Delivery charge")
    print("total amount:",a)  '''
'''
mark1=float(input("Enter the marks for subject1="))
mark2=float(input("Enter marks for subject2="))
mark3=float(input("Enter the marks for subject3="))
if mark1 > 40 and mark2 > 40 and mark > 40:
    print("Promoted")
else:
    print("Not Promoted")'''   
'''
weather=input("Enter the today's weather condition (Rainy/Sunny)") 
if weather=="Rainy" or weather=="Sunny":
    print("Bring Umbrella")
else:
    print("No umbrella needed")'''    

'''
day = input("Enter the day=")

if day == "Sunday":
    print("Weekend")
elif day == "Tuesday":
    print("Week day")
elif day == "Wednesday":
    print("Week day")
elif day == "Thursday":
    print("Week day")
elif day == "Friday":
    print("week day")
elif day == "Saturday":
    print("Weekend")    
else:
    print("Invalid") '''

  
'''
number = int(input("Enter the number="))
if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("number is zero")'''
'''
x=int(input("Enter the value="))
if x==5:
    print("you are lucky")
else:
    print("program ends")

positive_num=0
x=int(input("Enter the number="))
if x > positive_num:
    print("Positive Number")
else:
    print("Not positive Number") 

vowel= input("Enter the letter=")

if vowel == "a" or vowel == "a":
    print("vowel letter")
elif vowel == "e" or vowel =="e":
    print("vowel letter")  
elif vowel == "i" or vowel == "i":
    print("vowel letter")  
elif vowel == "o" or vowel == "o":
    print("vowel letter")
elif vowel == "u" or vowel == "u":
    print("vowel letter")
else:
    print("consonant") 

x=int(input("Enter the number="))
if x % 2:
    print("odd number")
else:
    print("even nuber") 

age = 18
x = int(input("Enter the value="))
if x  > 18:
    print("your vote eligible")
else:
    print("your vote not eligible")   

a = int(input("Enter the a value="))
b = int(input("Enter the b value="))    
if a > b:
    print("a is greater than", a)
else:
    print("b is greater than", b)

a = int(input("Enter the a value="))
b = int(input("Enter the b value="))
if a < b:
    print("a is less than", a)
else:
    print("b is less than", b) 

tara = int(input("Enter the number="))
jothi = int(input("Enter the number="))
total = tara + jothi
if total % 5 == 0:
    print("1")
else:
    print("0")  

n = int(input("Enter the Number="))
if n % 7:
    print("Yes")
else:
    print("No")

amount = 500
x = int(input("Enter order amount="))
if amount >= 500:
    print("extra delivery charge is: 50")
else:
    print("total amount:", a+50) 

day = int(input("How many day you with take books="))
freeday = 7
if day > freeday:
    print("fine no charge") 
else:
    print("You no fine take some books") 

attendance = float(input("Enter the attendance"))
average = int(input("Enter the average"))
if average >=75 and average >= 40:
    print("your Eligible")
else:
    print("your not Eligible")  

a = int(input("Enter a the mark="))
b = int(input("Enter b the mark="))
c = int(input("Enter c the mark="))


if a >= 75:
    print("You got an A grade")
elif b >= 60:
    print("You got a B grade")
elif c >= 45:
    print("You got a C grade")    
else:
    print("You didn't get an A,B or C grade") 

mark = int(input("Enter the mark="))

if mark >= 75:
    print("you got an A grade")
elif mark >= 60:
    print("you got an B grade") 
elif mark >= 45:
    print("you got a C grade")
else:
    print("you didn't get an A,B or C grade") 

mark1 = float(input("Enter the mark subject1="))
mark2 = float(input("Enter the mark subject2=")) 
mark3 = float(input("Enter the mark subject3="))  

if mark1 > 40 and mark2 > 40 and mark3 > 40:
    print("Promoted")
else:
    print("Not promoted")    

weather = input("Enter the today's weather condition (rainy/sunny)=")
if weather == "rainy" or weather == "sunny":
    print("Bring umbrella")
else:
    print("No umbrella needed")   

day = input("Enter a day of the week=")
if day == "saturday" or day == "sunday":
    print("Holiday")
else:
    print("No umbrella needed")  


#First, the program checks if the mark is greater than or equal to 90.

# If True, print "Excellent performance".

# If the first condition is not true, check if the mark is greater than or equal to 75.

# If True, print "Very good performance".

# If the second condition is not true, check if the mark is greater than or equal to 50.

# If True, print "Good performance".

# If none of the above conditions are true (i.e., mark < 50),
#  print "Needs improvement".

mark = int(input("Enter the marks="))

if mark >= 90:
    print("excellent performance")
elif mark >= 75:
    print("very good performance")    
elif mark >= 50:
    print("good performance")    
elif mark < 50:
    print("needs improvement") 

# If the temperature is greater than or equal to 35°C, print "It's extremely hot!"

# If the temperature is greater than or equal to 25°C but less than 35°C, print "It's a warm day."

# If the temperature is greater than or equal to 15°C but less than 25°C, print "The weather is pleasant."

# If the temperature is less than 15°C, print "It's cold outside."

temperature = int(input("Enter the temperature="))

if temperature >= 35:
    print("It's extremely hot")
elif temperature >= 25:
    print("It's a warm day")
elif temperature >= 15:
    print("The weather is pleasant")
else:
    print("It's cold outside")   ''' 

vowels = input("Enter the letter: ")

match vowels:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("The character is a vowel.")
    case _:
        print("The character is not a vowel.") 

vov = input("Enter the letter=")
match vov:
    case 'a' | "A":
        print("vowels letter")
    case 'e' | "E":
        print("vowels letter") 
    case 'i' | "I":
        print("vowels letter")
    case 'o' | "O":
        print("vowels letter")
    case 'u' | "U":
        print("vowels letter")
    case _:
        print("consonat")       
          




 

