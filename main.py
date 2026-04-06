import sys
import LCS


def main():
    return 

if __name__ == "__main__":
    main()
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
                weights[strippedLine[0]] = strippedLine[5: len(strippedLine)]

            #strings for comparison
            else:
                if not strA:
                    strA = strippedLine[4: len(strippedLine)]
                else:
                    strB = strippedLine[4: len(strippedLine)]

    print("weights: ", weights)
    print("string A: ", strA)
    print("string B: ", strB)

    LCS.LongestCommonSubsequence(strA, strB, weights)