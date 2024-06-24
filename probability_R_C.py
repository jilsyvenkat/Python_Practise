from typing import List


# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    # Write your code here
    total_cels = R * C
    available_ones = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] == 1:
                available_ones += 1
    print(available_ones)
    probability = format((available_ones / total_cels), '.8f')
    print(probability)
    return probability

getHitProbability(2, 3, [[0, 0, 1], [1, 0, 1]])
# getHitProbability(2,2,[[1,1],[1,1]])
