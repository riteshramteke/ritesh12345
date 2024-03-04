

# form flask import Flask ,request,jsonnify
# app=Flask(__name__)

# @app.route("/",method=["POST"])
# def square_number():
#     if request.method=='POST':
#         try:
#             data=request.get_json()
#             number=data['number']

#             if not isinstance(number,(int)):
#                 return jsonnify({'message':'please enter a valid integer'}),400
            
#             result =number**2
#             return jsonnify({"result":result})
#         except KeyError:
#             return jsonnify({ "error":"Please provide the required details"}),400
#         except Exception as e:
#             return jsonnify({"error":str(e)}),400
#     else:
#         return jsonnify({"error":'only post'}),405
# if __name__== "__main__":
#   app.run(debug=True)








# string = 'ksahkjsfniwuofsjdkjwbfmnfiwhfdnxkajshiwkowhjnfkjnzkjvmnasijkfs'
# lst1 = []
# for i in string:
#     if i not in lst1:
#         lst1.append(i)
# for j in lst1:
#     print(j,string.count(j))






# N = 3  # Set the value of N

# for i in range(1, N + 1):
#     # Print 'A' repeated i times, then a newline character
#     print('A' * i)

# for i in range(N - 1, 0, -1):
#     # Print 'A' repeated i times, then a newline character
#     print('A' * i)


# N = 3  # Set the value of N

# for i in range(1, N + 1):
#     # Print 'A' repeated i times, followed by a space
#     line = 'A' * i
#     # Print the line twice with a space in between
#     print(line, line)




# s = "Abhijicpadbibhsjoicjocisishvojiojoijoohnojzojnakbiksbfowhnowohnrjwobbfbcjkb kbc kvb kjbknjneojnbcjncincn"
# unique_letters = sorted(set(char.lower() for char in s if 'a' <= char.lower() <= 'z'))
# print(unique_letters)

# s = "Abhijicpadbibhsjoicjocisishvojiojoijoohnojzojnakbiksbfowhnowohnrjwobbfbcjkb kbc kvb kjbknjneojnbcjncincn"

# # Initialize an empty list to store unique lowercase letters
# unique_letters = []

# # Iterate through each character in the string
# for char in s:
#     # Check if it's an uppercase letter ('A' to 'Z')
#     if 'A' <= char <= 'Z':
#         # Convert it to lowercase ('a' to 'z')
#         lowercase_char = chr(ord(char) + 32)

#         # Check if the lowercase letter is not already in the unique_letters list
#         if lowercase_char not in unique_letters:
#             # Append it to the unique_letters list
#             unique_letters.append(lowercase_char)

# # Convert the list to a string (optional, for alphabetical order)
# unique_letters_str = ''.join(unique_letters)

# # Print the unique lowercase letters
# print(unique_letters_str)

# s = "Abhijicpadbibhsjoicjocisishvojiojoijoohnojzojnakbiksbfowhnowohnrjwobbfbcjkb kbc kvb kjbknjneojnbcjncincn"

# # Initialize an empty string to store sorted alphabets
# sorted_alphabets = ""

# # Iterate through the string and add alphabets to the sorted_alphabets string
# for char in s:
#     if char.isalpha():
#         # Check if the character is not already in the sorted string
#         if char not in sorted_alphabets:
#             # Find the correct position to insert the character
#             insert_index = 0
#             while insert_index < len(sorted_alphabets) and char > sorted_alphabets[insert_index]:
#                 insert_index += 1
#             # Insert the character at the correct position
#             sorted_alphabets = sorted_alphabets[:insert_index] + char + sorted_alphabets[insert_index:]

# # Now, sorted_alphabets contains the sorted alphabets from 'A' to 'Z'
# print(sorted_alphabets)


























































# l=[1,2,3,4,5,5,4,3,2,1]
# l2=[]
# for i in l:
#  if i not in l2:
#   l2.append(i)
# print(l2)

































