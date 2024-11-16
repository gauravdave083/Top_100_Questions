# Write the program to count the frequency of elements in an array in python programming language. We are given with an array and need to print each element along its frequency.

class Solution:
     def findFrequency(self, arr):
          frequency = {}
          
          for elem in arr:
               if elem in frequency:
                    frequency[elem] += 1
               else:
                    frequency[elem] = 1
          return frequency