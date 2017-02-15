A = [1,2,3,6]
B = [4,5]
A_ind = 0
B_ind = 0
res = []
while A[-1] == None:
    del A[-1]
while A[A_ind] and B[B_ind]:
    if A[A_ind] < B[B_ind]:
        res.append(A[A_ind])
        A_ind += 1
    else:
        res.append(B[B_ind])
        B_ind += 1       
    if A_ind == len(A) or B_ind == len(B):
        break
if A_ind == len(A):
    res.extend(B[B_ind:])
elif B_ind == len(B):
    res.extend(A[A_ind:])
    
print res