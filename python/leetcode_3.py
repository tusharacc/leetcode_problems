def lengthOfLongestSubstring( s: str) -> int:
    #prev = ''
    substring = ''
    max_length = 0
    for c in s:
        #print (substring,c)
        #if prev != c:
        if c not in substring:
            substring += c
        else:
            length = len(substring)
            max_length = length if length > max_length else max_length
            substring = substring.split(c)[1] + c
        #else:
        #    length = len(substring)
        #    max_length = length if length > max_length else max_length
        #    substring = c
        #prev = c
    #print ("substring",substring)
    if len(substring) > max_length:
        max_length = len(substring)
    return max_length

if __name__ == '__main__':
    print (lengthOfLongestSubstring("cdd"))
    print (lengthOfLongestSubstring("abcabcbb"))
    print (lengthOfLongestSubstring("bbbbb"))
    print (lengthOfLongestSubstring(" "))
    print (lengthOfLongestSubstring("dvdf"))
            