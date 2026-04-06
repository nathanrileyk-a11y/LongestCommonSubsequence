import sys
import LCS
import time

start = time.time() #used for testing runtime of test files


if __name__ == "__main__":
    
    testFile = "test-files/" + sys.argv[1]
    numLines = sum(1 for line in open(testFile))
    lastLine = numLines-1
    weights = {}
    strA = ""
    strB = ""

    with open(testFile) as file:
        for line in file:
            strippedLine = line.rstrip()

            if not strippedLine:
                continue

            #weight values
            if(strippedLine[0].islower()):
                weights[strippedLine[0]] = int(strippedLine[5: len(strippedLine)])

            #strings for comparison
            else:
                if not strA:
                    strA = strippedLine[4: len(strippedLine)]
                else:
                    strB = strippedLine[4: len(strippedLine)]

    weight, common_subsequence = (LCS.LongestCommonSubsequence(strA, strB, weights).compute())
    print(weight)
    print(common_subsequence)

    end = time.time()
