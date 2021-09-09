# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
class Solution(object):
    def minFlips(self, mat):
        M = len(mat)
        N = len(mat[0])
        MN = M*N
        neighbours = [None for _ in range(MN)]
        matcode = 0
        
        for r in range(M):
            for c in range(N):
                i = r*N + c
                l = [i]
                if r>0: l.append(i-N) #UP
                if r<M-1: l.append(i+N) #DOWN
                if c>0: l.append(i-1) #LEFT
                if c<N-1: l.append(i+1) #RIGHT
                
                neighbours[i] = sum(1<<t for t in l)
                matcode |= (mat[r][c]<<i)
                
                     
        best = MN + 1
        for pattern in range(2**MN):
            m = 0
            steps = 0
            for t in range(MN):
                if pattern & (1 << t):
                    m ^= neighbours[t]
                    steps +=1
                    
                if m == matcode:
                    best = min(best, steps)
                    break
        return best if best <=MN else -1
