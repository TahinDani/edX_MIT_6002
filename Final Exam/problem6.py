from numpy import zeros, int


def permutations(n, length):
    numbers = range(n)
    permutations = n**length
    output = zeros((permutations, length), dtype=int)

    for i in range(length):
        t2 = n**i
        p1 = 0
        while (p1 < permutations):
            for al in range(n):
                for p2 in range(t2):
                    output[p1, i] = numbers[al]
                    p1 += 1
    return output


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    result_x_choices = 0
    all_permutations = permutations(2, len(choices))
    for result in all_permutations:
        for i in range(len(result)):
            result_x_choices += result[i]*choices[i]
            sum_of_result = sum(result)
        # TODO: check if any of the result_x_choices == total
        print(result_x_choices)
    

print(find_combination([1,2,2], 1))

