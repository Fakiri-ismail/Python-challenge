import numpy as np

# Number of Dice Rolls With Target Sum
def numRollsToTarget(n: int, k: int, target: int) -> int:
    mat = np.zeros([n+1, target+1])
    mat[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            for t in range(target, j-1 , -1):
                if mat[i-1][t-j] != 0:
                    mat[i][t] += mat[i-1][t-j]
                    mat[i][t] = mat[i][t] % (10**9 + 7)
    return int(mat[n][target])


if __name__=='__main__':
    case1 = numRollsToTarget(2, 6, 7)
    case2 = numRollsToTarget(30, 30, 300)
    print(case1)
    print(case2)