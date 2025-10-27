# Question-1
# n = int(input("Enter the n value="))
# if 0 < n:
#     print("Positive number")
# elif 0 > n:
#     print("Negative number")
# else:
#     print("Zero")

# Question-2
# n = int(input("Enter the n value="))
# if n % 2 == 0:      
#     print("Even")                            
# else:         
#     print("Odd")    

# Question-3
# n = int(input("Enter the n value="))
# m = int(input("Enter the m value="))
# if n > m:
#     print(n)
# else:
#     print(m)    
   
# Question-4
n = int(input("Enter the n value="))
m = int(input("Enter the m value="))
o = int(input("Enter the o value="))
if n < m and n > m:
    print(n)
elif m > o:
    print(m)
else:
    print(o)      

# a = int(input("Enter the a value="))
# b = int(input("Enter the b value="))
# c = int(input("Enter the c value="))
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# elif c>a and c>b:
#     print(c)  

# question-5 
# a = int(input("Enter the a value="))
# b = int(input("Enter the b value="))
# c = int(input("Enter the c value="))
# d = int(input("Enter the d value="))
# if a > b and a > c and a > d:
#     print(a)
# elif b > a and b > c and b>d:    
#     print(b)
# elif c >a and c>b and c>d:    
#     print(c)
# else :    
#     print(d)

# Question-6
# n = int(input("Enter the n value="))
# if n % 5 ==0:
#     print("Divisiable number")
# else:
#     print("Not Divisiable number")    

# question-7
# n = int(input("Enter the n value="))
# if n % 5==0 or n % 3 == 0:
#     print("diviable number")
# else:
#     print("not diviable number")    

# question-8
# vowels = (input("Enter the vowels letter="))
# if vowels == "a" or vowels == "e" or vowels == "i" or vowels == "o" or vowels == "u":
#     print("vowels letter")
# else:
#     print("not vowels letter")    

# question-9
# n = int(input("Enter the number="))
# if ((n % 4 == 0 and n % 100!=0) or n % 400==0):
#     print("Leap year")
# else:
#     print("Not leap year")    

#question-10
# n = int(input("Enter the number="))
# if n>=18:
#     print("your vote eligible")
# else:
#     print("your not eligible vote")    

# question-11
# n = int(input("Enter the n value="))
# if n >= 35:
#     print("Pass")
# else:
#     print("Fail")  
 
# question-12  
# temperature = int(input("Enter the value="))
# if temperature >= 100:
#     print("Fever")
# else:
#     print("Normal")

# question-13
# n = int(input("Enter the n value="))
# if n % 3 == 0 or n % 5 == 0:
#     print("divisible number")
# else:
#     print("not divisible number")    

# question-14
# gender = input("Enter gender (M/F): ")
# if gender == 'M' or gender == 'm':
#     print("Male")
# elif gender == 'F' or gender == 'f':
#     print("Female")
# else:
#     print("Invalid Input")    

# question - 15    
# check = input("Enter the letter: ")
# if check>='A' and check<='Z':
#     print("uppercase letter")
# elif check >= 'a' and check <= 'z':
#     print("lowercase letter")
# else:
#     print("Not alphet letter")        

# question - 15
# check = int(input("Enter the number="))
# if check >= 2 and check <= 10:
#     print("Intha number 2 ela irundhu 10 varairukku")
# else:
#     print("Ithu illa")    

# question-16
# password = int(input("Enter the password: (storing/weak)"))
# if password >= 8:
#     print("Strong password")
# else:
#     print("Weak password")    

# question-17
# n = int(input("Enter the n value="))
# if n > 0 and n % 2 == 0:
#     print("positive and even")
# else:
#     print("not negative and even")    

# question-18
# n = int(input("Enter the n value="))
# if n < 0 and n % 2 != 0:
#     print("Positive and Odd")
# else:
#     print("not Negative and Odd")    

# question-19
# t = int(input("Enter the tamil marks="))
# e = int(input("Enter the english marks="))
# m = int(input("Enter the maths marks="))
# p = int(input("Enter the physics marks="))
# c = int(input("Enter the chemistry marks="))
# b = int(input("Enter the biology marks="))

# total = (t+e+m+p+c+b)/6
# print("total marks=", total)

# BMI = weight / (height * height)
# weight = float(input("Enter the weight="))
# height = float(input("Enter the height="))
# height = height/100
# bmi = weight / (height*height)
# print("Enter the human BMI", bmi)

# Program to get human age, height, weight and calculate BMI
# Program to get human age, height, weight and calculate BMI

# Get user input
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# weight = float(input("Enter your weight in kilograms: "))
# height_cm = float(input("Enter your height in centimeters: "))

# # Convert height to meters
# height = height_cm / 100

# # Calculate BMI
# bmi = weight / (height * height)

# # Display information
# print("\n--- Human Info ---")
# print("Name:", name)
# print("Age:", age, "years")
# print("Weight:", weight, "kg")
# print("Height:", height_cm, "cm")
# print("BMI:", round(bmi, 2))

# # BMI category
# if bmi < 18.5:
#     bmi_category = "Underweight"
# elif bmi >= 18.5 and bmi < 25:
#     bmi_category = "Normal weight"
# elif bmi >= 25 and bmi < 30:
#     bmi_category = "Overweight"
# else:
#     bmi_category = "Obese"

# print("BMI Category:", bmi_category)

# # Age group classification
# if age < 13:
#     age_group = "Child"
# elif age >= 13 and age < 20:
#     age_group = "Teenager"
# elif age >= 20 and age < 60:
#     age_group = "Adult"
# else:
#     age_group = "Senior"

# print("Age Group:", age_group)


# j = int(input("enter the j value="))
# s = 0 
# n = j

# while j > 0:
#     r = j % 10
#     s = s + r*r*r
#     j = j // 10
#     if n == s:
#         print("armstrong number")
#     else:
#         print("not armstrong number")
   

# n = int(input("Enter the n value = "))
# s = 0
# p = n

# while n > 0:
#     r = n % 10
#     s = s * 10 + r
#     n = n // 10

# if p == s:
#     print("Polyndrome number")
# else:
#     print("Not Polyndrome number")
 
# n = int(input("Enter a number: "))
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print(n, "is not a prime number")
#     else:
#         print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")

# f=input("pizza/burger/sandwich:")
# n=int(input("enter a number:"))
# if f=="pizza":
#     cast=200
#     tax=(5/100)*cast
#     print("amount:",cast*n+tax*n)
# elif f=="burger":
#     cast=100
#     tax=(5/100)*cast
#     print("amount:",cast*n+tax*n)
# elif f=="sandwich":
#     cast=50
#     tax=(5/100)*cast
#     print("amount:",cast*n+tax*n)



