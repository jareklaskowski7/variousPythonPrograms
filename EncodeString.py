"""
Given an input string, write a function that returns the Run Length Encoded string for the input string.
For example, if the input string is ‘wwwwaaadexxxxxx’, then the function should return ‘w4a3d1e1x6’.
Str = ‘abccccedfffghegggg’
"""


def encodeString(word):
    encodedWord = str()
    counter = 1
    for idx in range(len(word)):
        if idx != (len(word) - 1) and word[idx] == word[idx + 1]:
            counter += 1
        else:
            encodedWord += word[idx]
            encodedWord += str(counter)
            counter = 1

    return encodedWord


encodedWord = encodeString("wwwwaaadexxxxxx")
print(encodedWord)

encodedWord = encodeString("abccccedfffghegggg")
print(encodedWord)
