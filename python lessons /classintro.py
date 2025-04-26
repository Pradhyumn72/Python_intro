# # # # Create a string
# # # my_string = "Hello, Pradhyumn!"

# # # # Get the length of the string using len()
# # # length_of_string = len(my_string)

# # # # Print the length
# # # print("The length of the string is:", length_of_string)
# # # Define the strings
# # string1 = "Becomes"
# # string2 = "becomes"
# # string3 = "BEAR"
# # string4 = "bEautiful"


# # substring = "be"


# # print(f'string1 starts with "{substring}": {string1.startswith(substring)}')
# # print(f'string2 starts with "{substring}": {string2.startswith(substring)}')
# # print(f'string3 starts with "{substring}": {string3.startswith(substring)}')
# # print(f'string4 starts with "{substring}": {string4.startswith(substring)}')
 
# # weight = 0.2
# # animal = "next"

# # result = "The weight of the " + animal + " animal is " + str(weight) + " kg."
# # print(result)

# # ex.2
# # def countB(word):
# #     return word.lower().count('b')

# # # Example usage:
# # result = countB("Bubble")
# # print(result)  # Output: 2

# # Q2
# # def count_letter(word,letter):
# #     return word.count(letter)
# # word ="hello"
# # letter = "l"
# # print(count_letter(word,letter))

# # Q3
# # def modify_case(word):
# #     return word.swapcase()
# # word = "HeLLo WoRLd"
# # print(modify_case(word))

# # hexadecimal converter
# def hex_to_binary(hex_num):
#     binary_num = bin(int(hex_num,16))[2:]
#     binary_num = (binary_num.zfill)(4*len(hex_num))
#     return binary_num
# hex_num = input("Enter a hexadecimal: ").strip()

# binary_result= hex_to_binary(hex_num)
# print(f"The binary equivalent of the hexadecimal{hex_num} is : {binary_result}")