import numpy as np


class LongestCommonSubsequence:
    def __init__(self, str1, str2, weights):
        self.A = str1
        self.B = str2
        self.n = len(str1)
        self.m = len(str2)
        self.arr = np.zeros((self.n+1, self.m+1), dtype=int)
        self.weights_dict = weights
    

    def longestCommonSubsequence(self):
        s = ""
        for i in range(self.n, -1, -1):
            for j in range(self.m, -1, -1):
                if i==self.n or j == self.m:
                    self.arr[i,j] = 0

                elif self.A[i] != self.B[j]:
                    self.arr[i,j] = max(self.arr[i, j+1], self.arr[i+1,j]) #there not equal so we cant take the letter
                else:
                    self.arr[i,j] = max(self.arr[i, j+1], self.arr[i+1,j], self.weights_dict[self.A[i]] + self.arr[i+1,j+1]) #the last value is when we choose this letter to be a part of the final subsequence
            i = 0
            j = 0



        


        