from collections import Counter

def Main():
    print("Give two words to check if they are anagrams")
    s1 = input()
    s2 = input()

    answer = isAnagram(s1, s2)
    print(answer)

    answer1 = isAnagram_counter(s1, s2)
    print(answer1)

    answer2 = isAnagram_sorted(s1, s2)
    print(answer2)

    Main()
    
def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    freq1 = {}
    freq2 = {}

    for let in freq1:
        if let in freq1:
            freq1[let] += 1
        else:
            freq1[let] = 1
    
    for let in freq2:
        if let in freq2:
            freq2[let] += 1
        else:
            freq2[let] = 1

    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False

    return True

def isAnagram_counter(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

def isAnagram_sorted(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

Main()