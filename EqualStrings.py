#

def equalStrings(s1, s2):
    areEqualStrings = False
    if len(s1) == len(s2):
        uniqueCharsOccurrences = {}

        for idx in range(len(s1)):
            if not s1[idx] in uniqueCharsOccurrences:
                uniqueCharsOccurrences[s1[idx]] = 1
            else:
                uniqueCharsOccurrences[s1[idx]] += 1

        for idx in range(len(s2)):
            if not s2[idx] in uniqueCharsOccurrences:
                break
            else:
                uniqueCharsOccurrences[s2[idx]] -= 1

        areEqualStrings = True
        for value in uniqueCharsOccurrences.values():
            if value != 0:
                areEqualStrings = False
                break

    return areEqualStrings


areEqualStrings = equalStrings("radar", "daras")
print(areEqualStrings)
areEqualStrings = equalStrings("radar", "darar")
print(areEqualStrings)
