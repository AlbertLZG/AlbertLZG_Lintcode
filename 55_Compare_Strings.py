class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        A_list = list(A)
        B_list = list(B)
        A_unique = list(set(A_list))
        B_unique = list(set(B_list))
        for i in B_unique:
            if i not in A_unique:
                return False
            num_B = B.count(i)
            num_A = A.count(i)
            if num_B > num_A:
                return False
        return True