# n = [1,2,3,4,5,6,7,8]
# even_sum = 0
# odd_sum = 0
# for num in n:
#     if num % 2 == 0:
#         even_sum = even_sum + num
#     else:
#         odd_sum = odd_sum + num

# print("Sum of Even Numbers", even_sum)
# print("Sum of Odd Numbers", odd_sum)    


# Question - 1
# n = [1,2,3,4,5,6]
# even = 0
# odd = 0
# for i in range(len(n)):
#     if n[i] % 2 ==0:
#         even = even + 1
#     else:
#         odd = odd + 1   
# print("Even Number=",even)
# print("Odd Number",odd) 


# n = ["Hii My Name is Nagaarjun"]
# for i in range(n-1):
#     print(i)

# n = "My Name is Nagaarjun"
# output = ""

# for i in range(len(n)-1, -1, -1):
#     output = output + n[i]

# print(output)



# n = "Cristiyano Ronaldo"
# o = ""
# for i in range(len(n)-1, -1, -1):
#     o = o + n[i]
# print(o)



# names = ["[ronaldo]", "messi", "Neymer", "Mbappe"]
# joined_str = ",".join(names)
# print(joined_str)


# sentences = ["My name is nagaarjun", "My brother name is anandhan"]
# # words = sentences.split(" ")

# for s in sentences:
#     words = s.split(" ")
#     for w in words:
#         print(w)


# text = "hello everyone"
# words = text.split()      
# reversed_words = words[::-1]  
# output = " ".join(reversed_words)  
# print(output)

# Question - 3
# n = "vankkam da Mapla"
# w = n.split()
# reversed_w = w[::-1]
# output = " ".join(reversed_w)
# print(output)

# Question - 2

def find_first_last(arr, target):
    first = -1
    last = -1

    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i

    return {"firstIndex": first, "lastIndex": last}


# Example
arr = [5, 2, 3, 5, 7, 5, 8]
target = 5
result = find_first_last(arr, target)
print(result)


