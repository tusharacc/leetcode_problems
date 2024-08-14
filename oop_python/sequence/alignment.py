from typing import List, Dict
import sys


# scoreMatrix: List[List[int]] = []

def calculateMinimumScore(string1: str, string2: str,gapPenalty:int=1):

    scoreMatrix = [[0 for _ in range(len(string1))] for _ in range(len(string2))]

    for i in range(len(string1)):
        scoreMatrix[i][0] = i*gapPenalty

    for j in range(len(string2)):
        scoreMatrix[0][j] = j*gapPenalty

    minimumScore:Dict[str,int] = {
        "value": sys.maxsize,
        "i":-1,
        "j":-1
    }
    for i in range(1,len(string1)):
        for j in range(1,len(string2)):
            mismatch:int = 1
            if string1[i] == string2[j]:
                mismatch = 0
            scoreMatrix[i][j] = min(scoreMatrix[i-1][j-1]+mismatch,scoreMatrix[i-1][j]+gapPenalty,scoreMatrix[i][j-1]+gapPenalty)

            if scoreMatrix[i][j] < minimumScore["value"]:
                minimumScore["value"] = scoreMatrix[i][j]
                minimumScore["i"] = i
                minimumScore["j"] = j

    return minimumScore["value"],minimumScore["i"],minimumScore["j"]

if __name__ == '__main__':
    print(calculateMinimumScore("AGTACG","ACATAG"))