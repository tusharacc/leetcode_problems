#@profile
def letterCombination(digits):
    letters = {
                "2": ["a","b","c"],
                "3": ["d","e","f"],
                "4": ["g","h","i"],
                "5": ["j","k","l"],
                "6": ["m","n","o"],
                "7": ["p","q","r","s"],
                "8": ["t","u","v"],
                "9": ["w","x","y","z"]
            }
    if len(digits) > 0:
    l = letters[digits[0]]
    #words = []
    firstPass = True

    for c in digits[1:]:
        temp = []
        for v in l:
            for item in letters[c]:
                temp.append(v+item)
        l = temp

    return l
else:
    return []

if __name__ == '__main__':
    letterCombination('2689')