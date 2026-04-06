# LongestCommonSubsequence
Nathan King - 72180427

Natahja Graddy - 69412034

## Run commands
Run input files with the following command:

**python main.py num.in (replace num with 1,2,3, example, etc.)**


input files should come from the test-files folder, so you do not have to worry about the path to the file as it is handled in the code.

## Written Solutions


## 1. Empirical Comparison


## Question 2. Recurrence Equation
The recurrence has base cases of 
DP[i, m] = DP[n, j] = 0 for all i,j, where n is number of rows and m is number of columns.

The recurrence relation is
DP[i, j] = max((DP[i+1,j]), DP[i, j+1], DP[i+1,j+1] + value(a_i)) if a_i = b_j
DP[i, j] = max(DP[i+1,j], DP[i, j+1]) if a_i != b_j


## Question 3. Big-Oh and Pseudocode
def HVLCS_len(A, B, weights)
    Build DP table using the recurrence relation
    totalLen = 0
    i, j = 0,0
    while i <n and j < m:
        if A_i = B_j
            if DP[i,j] = DP[i+1, j+1] + weights[A[i]]:
                totalLen, i, j += 1
            elif DP[i,j] == DP[i+1, j]:
                i +=1
            else
                j += 1
        else
            if DP[i,j] == DP[i+1, j]:
                i +=1
            else
                j += 1
    return totalLen

this gives the length of the final string using backtracking instead of returning the string itself
        