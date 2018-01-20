def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    l = len(L)
    subsequents = []
    for n in range(1, l+1):
        subsequents.append([sum(L[i:i+n]) for i in range(len(L)-n+1)])
    #print(subsequents)
    result = 0
    for outer in subsequents:
        for inner in outer:
            if inner > result:
                result = inner
    #print(result)

L = [3, 4, -8, 15, -1, 2]
max_contig_sum(L)