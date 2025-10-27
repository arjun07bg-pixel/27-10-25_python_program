# question -1
# a = int(input("Enter the a value="))
# b = int(input("Enter the b value="))
# for i in range(a, b+1):
#     print(i)

# a = int(input("Enter the a value="))
# b = int(input("Enter the b value="))
# while a<=b:
#     print(a)
#     a = a+1

# question -2
# a = int(input("Enter a value="))
# b = int(input("Enter b value="))
# for i in range(a, b-1,-1):
#     print(i)

# a = int(input("Enter a value="))
# b = int(input("Enter b value="))
# while a >= b:
#         print(a)
#         a = a - 1
    
# question -3
# a = int(input("Enter the a value="))
# b = int(input("Enter the b value="))
# for i in range(a,b):
#     if i % 2 == 0:
#         print(i)

# a = int(input("Enter the a value="))
# b = int(input("Enter the b value="))
# while a <= b:
#     if a % 2 == 0:
#         print(a)
#         a = a+2

# question -4
# a = int(input("Enter the a value="))
# b = int(input("Enter the b value="))
# n = int(input("Enter the n value="))
# while a<=b:
#     if a % n == 0:
#         print(a)
#     a = a+2
   
# question - 5
# a = int(input("Enter the a value="))
# b = int(input("Enter the b value="))
# n = b
# while a <= n:  
#     if n % 2 == 1:
#         print(n)
#     n=n-1

# question - 6  
# a = int(input("Enter a value="))
# b = int(input("Enter b value="))
# c = 0
# for i in range(b, a - 1, -1):
#     if i % 2 != 0:
#         c = c + 1
# print("Total odd numbers:", c)

# question -7       
# a = int(input("Enter the a value="))
# b = int(input("Enter the b value="))
# n = int(input("Enter the n value="))
# c = 0
# for i in range (a,b+1):
#     if i % n == 0:
#         c = c + 1
# print(c)        

# question -8
# a = int(input("Enter the a value="))
# b = int(input("Enter the b value="))
# sum = 0
# for i in range(a,b+1):
#     sum=sum+i
#     a=a+1


# n = int(input("Enter the n value="))
# i = 1
# while i <= n:
#     print(i, "x", n, "=", i*n)
#     i = i + 1

# question-9
# n = int(input("Enter the n value="))
# total = 0
# for i in range(1, n + 1):
#     total = total + i
# print("Sum from 1 to", n, "=", total)

# question - 10   
# n = int(input("Enter the n value: "))
# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i
#     i = i + 1
# print("Factorial number =", fact)

# question - 11
# distance = int(input("Enter the distance="))
# if distance <= 10:
#     fare = distance * 15
# elif distance <= 30:
#     fare = (10 * 15) + (distance - 10) * 12
# else:
#     fare = (10 * 15) + (20 * 12) + (distance - 30) * 10

# print("Total fare  Rs->", fare) 

# question - 12           
# def total_reward(steps):
#     reward = (steps // 1000) * 5
#     if steps >= 5000:
#         reward += reward * 0.2   # add 20% bonus
#     print(reward)

# total_reward(4000)
# total_reward(6000)
# total_reward(10000)

# def water_level(minutes):
#     level = 0       # initial water level
#     for i in range(minutes):
#         level = level + 7   # fills 7 liters
#         level = level - 3   # leaks 3 liters
#         if level > 100:
#             level = 100  # cannot exceed max capacity
#             break
#     print("Water level after", minutes, "minutes:", level, "liters")

# # Test cases
# water_level(1)    
# water_level(10)   
# water_level(30)   



