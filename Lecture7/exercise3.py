def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    length_sum = 0
    quantity = 0
    for word in L:
        length_sum += len(word)
    mean = length_sum / float(len(L))
    #print(mean)
    for t in L:
        quantity += (len(t)-mean)**2
    #print(quantity)
    std = (quantity / len(L))**0.5
    return std

#[10, 4, 12, 15, 20, 5
L = ['aaaaaaaaaa', 'aaaa', 'aaaaaaaaaaaa', 'aaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaa', 'aaaaa']
print(stdDevOfLengths(L))

print(stdDevOfLengths(L) / 11)