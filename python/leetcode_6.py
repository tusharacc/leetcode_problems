@profile
def convert(s,numRows):
    l = []
    row = 0
    temp = []
    spaces = 0
    for i,c in enumerate(s):
        if spaces == 0:
            temp.append(c)
            row += 1
        else:
            temp = [""]*numRows
            temp[spaces] = c
            row = numRows
        
        if row >= numRows:
            row = 0
            l.append(temp)
            temp = []
            if spaces == 0:
                spaces = numRows - 2
            else:
                spaces -= 1
    
    if row < numRows:
        while (row < numRows):
            temp.append("")
            row += 1
    l.append(temp)
    index = 0
    output_str = ""
    while index < numRows:
        for i in l:
            output_str += i[index]
        index += 1
        
    return output_str

if __name__ == '__main__':
    print(convert("PAYPALISHIRING",3))
    print(convert("PAYPALISHIRING",4))
    print(convert("AB",1))
    print(convert("AB",2))
    