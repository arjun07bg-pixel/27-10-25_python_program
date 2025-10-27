# Question - 1
# n = int(input("Enter the n value="))
# m = int(input("Enter the m value="))
# total = n + m
# if total % 2 == 0:
#     print("even")
# else:
#     print("odd")    

# Question - 2
# n = int(input("Enter the 2 digit number="))
# first_digit = n // 10
# second_digit = n % 10
# m = first_digit + second_digit
# j = first_digit * second_digit
# if m + j == n:
#     print("Great")
# else:
#     print("No")  

# Question - 3

# residential = "residential"
# commercial = "commercial"
# consumertype = input("enter the consumer value:")
# units = int(input("enter the unit:"))
# if consumertype == residential:
#    if units < 100:
#         print(units * 5)
#    elif units > 100 and units < 200:
#         print(units * 7)
#    elif units > 200:
#         print(units * 10)

# if consumertype == commercial:
#    if units < 100:
#         print(units * 3)
#    elif units > 100 and units < 200:
#         print(units * 5)
#    elif units > 200:
#         print(units * 7)

# Question - 4
# distance = int(input("Enter a value="))
# if distance <= 5:
#     print("50") 
# elif distance > 6 and distance < 15:
#     print(distance*8)    
# elif distance > 15:
#     print(distance*6)

# # Question - 5
# n = int(input("Enter the n value="))
# m = int(input("Enter the m value="))
# x = int(input("Enter the x value="))

# if n==m and n==x and x==n:
#     print("all three sides are equal")
# elif n==m and m==n:
#     print("any two sides are equal")
# elif n!=m and m!=x and x!=n:
#     print("all three sides are different")        

# Question - 6
# number = int(input("Enter the number = "))

# if number % 3 == 0 and number%5==0:
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)

# Question - 7

# course = input("Enter the course (Science/Commerce/Arts): ")

# match course:
#     case "Science":
#         sub = input("Enter your choice (Medical/Engineering): ")
#         match sub:
#             case "Medical":
#                 print("Chosen Path: Science → Medical")
#             case "Engineering":
#                 print("Chosen Path: Science → Engineering")
#             case _:
#                 print("Invalid sub-choice for Science")

#     case "Commerce":
#         sub = input("Enter your choice (CA/B Com): ")
#         match sub:
#             case "CA":
#                 print("Chosen Path: Commerce → CA")
#             case "B Com":
#                 print("Chosen Path: Commerce → B Com")
#             case _:
#                 print("Invalid sub-choice for Commerce")

#     case "Arts":
#         sub = input("Enter your choice (History/Literature): ")
#         match sub:
#             case "History":
#                 print("Chosen Path: Arts → History")
#             case "Literature":
#                 print("Chosen Path: Arts → Literature")
#             case _:
#                 print("Invalid sub-choice for Arts")

#     case _:
#         print("Invalid course entered")

# Question - 8
# time = int(input("Enter the show time (24-hour format): "))
# if  9 <= time < 12:
#     print("Morning show")
# elif 12 <= time < 16:
#     print("Matinee show")
# elif 16 <= time < 20:
#     print("Evening show")
# else:
#     print("Night show")         
 
# Question - 9
# km=float(input("Enter the kilometer"))
# choice=int(input("Choose conversion:1_meter,2_centimeter,3_millimeter,4_miles: "))
# match choice:
#   case 1:
#     print(km*1000,"meter")
#   case 2:
#     print(km*100000,"centimeter")
#   case 3:
#     print(km*1000000,"millimeter")
#   case 4:
#     print(km*0.621371,"miles")
#   case _:
#     print("invalid conversion")

# Question - 10
# payment_mode = input("Enter your payment mode (UPI/Card/NetBanking/COD): ")

# match payment_mode:
#     case "UPI":
#         print("You selected UPI payment")
#     case "Card":
#         print("You selected Debit/Credit Card payment")
#     case "NetBanking":
#         print("You selected Net Banking")
#     case "COD":
#         print("You selected Cash on Delivery")
#     case _:
#         print("Invalid Payment Mode")      




# n = 8
# counter = 1
# while counter <= n:
#     print(n)
#     n=n-2
    
# n = 8 
# counter = n
# end_value = 0
# output = ""
# while counter > end_value:
#     output = output+str(counter)+" "
#     counter = counter-1
# print(output)

# surya method
# n = 8 
# counter = n
# end_value = 0
# output = ""
# while counter > end_value:
#     print(counter, end=" ")
#     counter = counter-1






