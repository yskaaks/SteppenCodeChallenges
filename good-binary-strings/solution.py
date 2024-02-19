"""
function largestGood(binString):
    Initialize a list to store substrings (goodSubstrings)
    Initialize a variable to keep track of the start of a current substring (start) = 0
    Initialize a counter for balance between '1's and '0's (balance) = 0

    for each index i in range of binString:
        if binString[i] is '1':
            increment balance
        else:
            decrement balance

        if balance is 0:
            Add the substring from start to i to goodSubstrings
            Set start to i+1 for the next substring

    Sort goodSubstrings based on the following criteria:
        - Substrings with a higher count of leading '1's come first
        - If equal, longer substrings come first

    Initialize largestGoodString as an empty string
    for each substring in goodSubstrings:
        Add substring to largestGoodString

    return largestGoodString
"""

# def isGoodBinaryString(binString):
#     ones = zeros = 0
#     for char in binString:
#         if char == "1":
#             ones += 1
#         elif char == "0":
#             zeros += 1

#         if zeros > ones:
#             return False

#     return ones == zeros


# def findLargestGoodString(binString):
#     # Split the string into good substrings
#     substrings = []  # This will hold tuples of (number of 1s, substring)
#     count = 0  # This will track the balance of 1s and 0s
#     start = 0  # Starting index of a substring

#     for i, char in enumerate(binString):
#         if char == "1":
#             count += 1
#         else:
#             count -= 1
#         if count == 0:
#             substrings.append((i - start + 1, binString[start : i + 1]))
#             start = i + 1

#     substrings.sort(reverse=True, key=lambda x: x[0])

#     # Reconstruct the string
#     largestGoodString = "".join([substring for _, substring in substrings])

#     return largestGoodString


# def largestGood(binString):
#     if isGoodBinaryString(binString):
#         return findLargestGoodString(binString)
#     else:
#         return "Input string is not a good binary string."


# test_string = "11011000"
# print(largestGood(test_string))
