class Solution:
    def strStr(self, source, target):
        # write your code here
        #compute prefix function
        if source == None or target == None:
            return -1
        else:
            pass
        
        m = len(target)
        pi = [0]
        k = 0
        if m == 0:
            return 0
        elif len(source) == 0:
            return -1
        else:
            pass

        for q in range(1,m):
            while k > 0 and target[k] != target[q]:
                k = pi[k-1]
                if target[k] == target[q]:
                    #k = k+1
                    break
                else:
                    pass
            if target[k] == target[q]:
                k = k+1
            else:
                pass
            pi.append(k)
            
        #KMP-match
        n = len(source)
        q = 0
        for i in range(n):
            while q > 0 and target[q] != source[i]:
                q = pi[q-1]
                if target[q] == source[i]:
                    #q = q+1
                    break
                else:
                    pass
            if target[q] == source[i]:
                q = q+1
            if q == m:
                return i-m+1
        return -1