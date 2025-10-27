
# question- 1
x = int(input("Enter the Number="))

if x % 2 == 0:
     print("Even number")
else:
     print("Odd number")    

# question - 2
team_score = int(input("Enter the team_score="))
target_score = int(input("Enter the target_score="))
over_left = int(input("Enter the over_left="))

if team_score >= target_score:
    print("Team wins by DL method")
if team_score < target_score or over_left > 0:
    print("Match to be continued")   
if team_score < target_score and over_left == 0:
    print("Team loses by DL method")    

# question - 3
a= int(input("Enter the leap year="))  

if a % 4 == 0:
    print("Y")
elif a % 400 == 0:
    print("y")
else:
    print("N")        

