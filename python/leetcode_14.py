def longestCommonPrefix(arr):
    d = {}
    for item in arr:
        end = 2
        while True:
            sub_str = item[0:end]
            if d.get(sub_str,None) == None:
                d[sub_str] = 1
            else:
                d[sub_str] += 1

            end += 1

            if end > len(item):
                break
    
    common_prefix = {key: value for key,value in d.items()  if value == len(arr) }

    longest_prefix = ''

    for key in common_prefix:
        if len(key) > len(longest_prefix):
            longest_prefix = key
    
    return longest_prefix

strs = ["dog","racecar","car"]
print (longestCommonPrefix(strs))

