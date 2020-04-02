#

def checkAnagrams(s1, s2):
    areAnagrams = True
    uniqueCharsOccurrences = {}
    for idx in range(len(s1)):
        if s1[idx] != " ":
            smallCharacter = s1[idx].lower()
            if not smallCharacter in uniqueCharsOccurrences:
                uniqueCharsOccurrences[smallCharacter] = 1
            else:
                uniqueCharsOccurrences[smallCharacter] += 1

    for idx in range(len(s2)):
        if s2[idx] != " ":
            smallCharacter = s2[idx].lower()
            if not smallCharacter in uniqueCharsOccurrences:
                break
            else:
                uniqueCharsOccurrences[smallCharacter] -= 1

    for value in uniqueCharsOccurrences.values():
        if value != 0:
            areAnagrams = False
            break

    return areAnagrams


areAnagrams1 = checkAnagrams("William Shakespeare", "I am a weakish speller")
print(areAnagrams1)
