def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    multipliers = []
    s2 = s
    for i in L:
        print("-------------------")
        temp_multiplier = int(s2/i)
        print(temp_multiplier)
        multipliers.append(temp_multiplier)
        s2 -= temp_multiplier*i
        print(s2)
    print(multipliers, sum(multipliers))
    if s2 == 0:
        print("Solution: " + str(sum(multipliers)))
    else:
        print("no solution")

L = [6, 5, 3, 2]
s = 346
greedySum(L, s)

