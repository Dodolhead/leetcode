class Solution(object):
    def isPowerOfTwo(self, n):
        y = 0
        while (n >= 2**y):
            if n == 2**y:
                break
            y += 1

        if n == 2**y :
            print("true")
        else: 
            print ("false")