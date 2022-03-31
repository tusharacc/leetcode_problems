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
    l = []
    #words = []
    firstPass = True
    for c in digits:
        if firstPass:
            for item in letters[c]:
                l.append(item)
            firstPass = False
        else:
            temp = []
            for v in l:
                for item in letters[c]:
                    temp.append(v+item)
            l = temp
                
        
    return l

if __name__ == '__main__':
    letterCombination('2689')