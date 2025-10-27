# Day 1
# Tara = int(input("Enter the number="))
# Jothi = int(input("Enter the number="))
# total = Tara + Jothi
# if total % 5 == 0:
#     print(0)
# else:
#     print(1)  

# N = int(input("Enter the Number="))
# if N % 7 == 0:
#     print("Yes")
# else:
#     print("No")

# amount=500
# a=int(input("Enter order amount="))
# if a <= 500:
#     print("extra delivery charge is:50")
#     print("total amount:",a+50)
# else:
#     print("No Delivery charge")
#     print("total amount:",a)  

#  Day 2

# vowels = input("Enter the letter: ")
# match vowels:
#     case 'a' | 'e' | 'i' | 'o' | 'u':
#         print("The character is a vowel")
#     case _:
#         print("The character is not a vowel") 

# vowels = input("Enter the letter= ")
# match vowels:
#     case 'a' | 'e' | 'i' | 'o' | 'u':
#         print("vowels letter")
#     case _:
#         print("not vowels letter")    

# vov = input("Enter the letter=")
# match vov:
#     case 'a' | "A":
#         print("vowels letter")
#     case 'e' | "E":
#         print("vowels letter") 
#     case 'i' | "I":
#         print("vowels letter")
#     case 'o' | "O":
#         print("vowels letter")
#     case 'u' | "U":
#         print("vowels letter")
#     case _:
#         print("consonat")      
          
# def age(x):
#     if x < 5 and x >= 0:
#         print("Free")
#     elif x >= 6 and x <= 12:
#         print(10)
#     elif x >= 13 and x <= 64:
#         print("20")
#     elif x >= 20 and x <= 100:
#         print(15)
#     else:
#         print("invalued input")
# age(8)
# age(90)
# age(-9)
# age(70)
# age(18) 

# def month(num):
#     match num:
#         case "1":
#             print("January")
#         case "2":
#             print("February")
#         case "3":
#             print("March")
#         case "4":
#             print("April")
#         case "5":
#             print("May")
#         case "6":
#             print("June")
#         case "7" :
#             print("July")
#         case "8":
#             print("August")
#         case "9":
#             print("September")
#         case "10":
#             print("October")
#         case "11":
#             print("November")
#         case "12":
#             print("December")
#         case _:
#             print("invalued input")
            
# num=input("Enter the month of variable:")
# month(num)


# a = int(input("Enter the kg weight(kg) "))
# if a <= 5:
#     print("shipping cost", 10 * 0.05 + 10)
# elif a <= 20:
#     print("shipping cose", 20 * 0.05 + 20)
# else:
#     print("shipping cose", 50 * 0.05 + 50)