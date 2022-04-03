#@profile
def convert(s, numRows):
    if numRows==1 or numRows>=len(s):
        return s

    d,ind=-1,0
    res=["" for i in range(numRows)]

    for i in s:
        if ind==0 or ind==numRows-1:
            d*=-1
        res[ind]+=i
        ind+=d

    return ''.join(res)

if __name__ == '__main__':
    print(convert("PAYPALISHIRING",3))
    print(convert("PAYPALISHIRING",4))
    print(convert("AB",1))
    print(convert("AB",2))