def isGoodBinaryString(binString):
    ones = zeros = 0
    for char in binString:
        if char == "1":
            ones += 1
        elif char == "0":
            zeros += 1

        if zeros > ones:
            return False

    return ones == zeros


def findLargestGoodString(binString):
    # Split the string into good substrings
    substrings = []  # This will hold tuples of (number of 1s, substring)
    count = 0  # This will track the balance of 1s and 0s
    start = 0  # Starting index of a substring

    # Identify all substrings
    for i, char in enumerate(binString):
        if char == "1":
            count += 1
        else:
            count -= 1
        if count == 0:
            substrings.append((i - start + 1, binString[start : i + 1]))
            start = i + 1

    # Sort substrings by length in descending order to ensure that larger substrings (which start with 1) are placed first
    substrings.sort(reverse=True, key=lambda x: x[0])

    # Reconstruct the string
    largestGoodString = "".join([substring for _, substring in substrings])

    return largestGoodString


def largestGood(binString):
    if isGoodBinaryString(binString):
        return findLargestGoodString(binString)
    else:
        return "Input string is not a good binary string."


test_string = "11011000"
print(largestGood(test_string))

# assert largestGood("11011000") == "11100100", "Test case 1 failed"
# assert largestGood("1100") == "1100", "Test case 2 failed"
# assert largestGood("1101001100") == "1101001100", "Test case 3 failed"

# print("All test cases passed.")
